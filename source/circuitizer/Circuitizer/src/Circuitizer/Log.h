#pragma once

#include <memory>
#include "Core.h"
#include "spdlog/spdlog.h"

namespace Circuitizer
{
	class CIRCUITIZER_API Log
	{
	public:
		static void Init();

		inline static std::shared_ptr<spdlog::logger>& GetCoreLogger() { return s_CoreLogger; }
		inline static std::shared_ptr<spdlog::logger>& GetClientLogger() { return s_ClientLogger; }

	private:
		static std::shared_ptr<spdlog::logger> s_CoreLogger;
		static std::shared_ptr<spdlog::logger> s_ClientLogger;
		
	};
}

// Core log macros...
#define CR_CORE_TRACE(...)  ::Circuitizer::Log::GetCoreLogger()->trace(__VA_ARGS__)
#define CR_CORE_INFO(...)   ::Circuitizer::Log::GetCoreLogger()->info(__VA_ARGS__)
#define CR_CORE_WARN(...)   ::Circuitizer::Log::GetCoreLogger()->warn(__VA_ARGS__)
#define CR_CORE_ERROR(...)  ::Circuitizer::Log::GetCoreLogger()->error(__VA_ARGS__)
#define CR_CORE_FATAL(...)  ::Circuitizer::Log::GetCoreLogger()->fatal(__VA_ARGS__)

// Client log macros...
#define CR_TRACE(...)       ::Circuitizer::Log::GetClientLogger()->trace(__VA_ARGS__)
#define CR_INFO(...)        ::Circuitizer::Log::GetClientLogger()->info(__VA_ARGS__)
#define CR_WARN(...)        ::Circuitizer::Log::GetClientLogger()->warn(__VA_ARGS__)
#define CR_ERROR(...)       ::Circuitizer::Log::GetClientLogger()->error(__VA_ARGS__)
#define CR_FATAL(...)       ::Circuitizer::Log::GetClientLogger()->fatal(__VA_ARGS__)
