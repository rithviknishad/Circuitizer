workspace "Circuitizer"
	architecture "x64"

	configurations
	{
		"Debug",
		"Release",
		"Dist"
	}

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

IncludeDir = {}
IncludeDir["GLFW"] = "Circuitizer/vendor/GLFW/include"

include "Circuitizer/vendor/GLFW"

project "Circuitizer"
		location "Circuitizer"
		kind "SharedLib"
		language "C++"
		
		targetdir ("bin/" .. outputdir .. "/%{prj.name}")
		objdir ("obj/" .. outputdir .. "/%{prj.name}")

		pchheader "crpch.h"
		pchsource "Circuitizer/src/crpch.cpp"

		files
		{
			"%{prj.name}/src/**.h",
			"%{prj.name}/src/**.cpp"
		}

		includedirs
		{
			"%{prj.name}/src",
			"%{prj.name}/vendor/spdlog/include",
			"%{IncludeDir.GLFW}"
		}

		links
		{
			"GLFW",
			"opengl32.lib"
		}

		filter "system:windows"
			cppdialect "C++17"
			staticruntime "On"
			systemversion "latest"

			defines
			{
				"CR_PLATFORM_WINDOWS",
				"CR_BUILD_DLL"
			}

			postbuildcommands
			{
				("{COPY} %{cfg.buildtarget.relpath} ../bin/" ..outputdir.. "/Sandbox")
			}

		filter "configurations:Debug"
			defines
			{
				"CR_DEBUG"
			}
			buildoptions "/MDd"
			optimize "On"

		filter "configurations:Release"
			defines "CR_RELEASE"
			buildoptions "/MDd"
			optimize "On"

		filter "configurations:Dist"
			defines "CR_DIST"
			buildoptions "/MDd"
			optimize "On"




project "Sandbox"
		location "Sandbox"
		kind "ConsoleApp"
		language "C++"
		
		targetdir ("bin/" .. outputdir .. "/%{prj.name}")
		objdir ("obj/" .. outputdir .. "/%{prj.name}")

		files
		{
			"%{prj.name}/src/**.h",
			"%{prj.name}/src/**.cpp"
		}

		includedirs
		{
			"Circuitizer/vendor/spdlog/include",
			"Circuitizer/src"
		}

		links
		{
			"Circuitizer"
		}

		filter "system:windows"
			cppdialect "C++17"
			staticruntime "On"
			systemversion "latest"

			defines
			{
				"CR_PLATFORM_WINDOWS",
			}

		filter "configurations:Debug"
			defines "CR_DEBUG"
			buildoptions "/MDd"
			optimize "On"

		filter "configurations:Release"
			defines "CR_RELEASE"
			buildoptions "/MDd"
			optimize "On"

		filter "configurations:Dist"
			defines "CR_DIST"
			buildoptions "/MDd"
			optimize "On"