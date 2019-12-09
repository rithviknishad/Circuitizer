#pragma once

#ifdef CR_PLATFORM_WINDOWS
	#ifdef CR_BUILD_DLL
		#define CIRCUITIZER_API __declspec(dllexport)
	#else
		#define CIRCUITIZER_API __declspec(dllimport)
	#endif // CR_BUILD_DLL
#else
	#error Circuitizer development only supports Windows 7 or above!
#endif // CR_PLATFORM_WINDOWS

#define BIT(x) (1 << x)