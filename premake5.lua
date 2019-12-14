workspace "Circuitizer"
	architecture "x64"
	startproject "Sandbox"

	configurations
	{
		"Debug",
		"Release",
		"Dist"
	}

outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

-- Include directories relative to root folder (solution directory)
IncludeDir = {}
IncludeDir["GLFW"] = "Circuitizer/vendor/GLFW/include"
IncludeDir["Glad"] = "Circuitizer/vendor/Glad/include"
IncludeDir["ImGui"] = "Circuitizer/vendor/imgui"
IncludeDir["glm"] = "Circuitizer/vendor/glm"

--group "Dependencies"
include "Circuitizer/vendor/GLFW"
include "Circuitizer/vendor/Glad"
include "Circuitizer/vendor/imgui"

project "Electrical"
	location "Electrical"
	kind "SharedLib"
	language "C++"
	staticruntime "off"

	targetdir ("bin/" ..outputdir .. "/%{prj.name}")
	objdir ("obj/" ..outputdir .. "/%{prj.name}")

	files
	{
		"%{prj.name}/src/**.h",
		"%{prj.name}/src/**.cpp"
	}

	includedirs
	{
		"Electrical/src",
	}

	postbuildcommands
	{
		("{COPY} %{cfg.buildtarget.relpath} ../bin/" ..outputdir.. "/Sandbox")
	}

	filter "system:windows"
		cppdialect "C++17"
		systemversion "latest"
		
		defines
		{
			"CR_PLATFORM_WINDOWS",
			"CR_BUILD_DLL",
		}

	filter "configurations:Debug"
		defines "CR_DEBUG"
		runtime "Debug"
		symbols "On"
		optimize "On"

	filter "configurations:Release"
		defines "CR_RELEASE"
		runtime "Release"
		optimize "On"

	filter "configurations:Dist"
		defines "CR_DIST"
		runtime "Release"
		optimize "On"

project "Circuitizer"
		location "Circuitizer"
		kind "SharedLib"
		language "C++"
		staticruntime "off"

		targetdir ("bin/" .. outputdir .. "/%{prj.name}")
		objdir ("obj/" .. outputdir .. "/%{prj.name}")

		pchheader "crpch.h"
		pchsource "Circuitizer/src/crpch.cpp"

		files
		{
			"%{prj.name}/src/**.h",
			"%{prj.name}/src/**.cpp",
			"%{prj.name}/vendor/glm/glm/**.hpp",
			"%{prj.name}/vendor/glm/glm/**.inl",
		}

		includedirs
		{
			"%{prj.name}/src",
			"%{prj.name}/vendor/spdlog/include",
			"%{IncludeDir.GLFW}",
			"%{IncludeDir.Glad}",
			"%{IncludeDir.ImGui}",
			"%{IncludeDir.glm}",
		}

		links
		{
			"GLFW",
			"Glad",
			"imGUI",
			"opengl32.lib"
		}

		filter "system:windows"
			cppdialect "C++17"
			systemversion "latest"

			defines
			{
				"CR_PLATFORM_WINDOWS",
				"CR_BUILD_DLL",
				"GLFW_INCLUDE_NONE"
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
			runtime "Debug"
			symbols "On"
			optimize "On"

		filter "configurations:Release"
			defines "CR_RELEASE"
			runtime "Release"
			optimize "On"

		filter "configurations:Dist"
			defines "CR_DIST"
			buildoptions "/MDd"
			optimize "On"




project "Sandbox"
		location "Sandbox"
		kind "ConsoleApp"
		language "C++"
		staticruntime "off"
		
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
			"Circuitizer/vendor",
			"Circuitizer/src",
			"%{IncludeDir.glm}",
		}

		links
		{
			"Circuitizer"
		}

		filter "system:windows"
			cppdialect "C++17"
			systemversion "latest"

			defines
			{
				"CR_PLATFORM_WINDOWS",
			}

		filter "configurations:Debug"
			defines "CR_DEBUG"
			runtime "Debug"
			symbols "On"
			optimize "On"

		filter "configurations:Release"
			defines "CR_RELEASE"
			runtime "Release"
			optimize "On"

		filter "configurations:Dist"
			defines "CR_DIST"
			runtime "Release"
			optimize "On"