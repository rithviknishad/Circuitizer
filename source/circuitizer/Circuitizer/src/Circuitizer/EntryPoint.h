#pragma once

#ifdef CR_PLATFORM_WINDOWS

extern Circuitizer::Application* Circuitizer::CreateApplication();

int main(int argc, char** argv)
{
	Circuitizer::Log::Init();

	CR_CORE_INFO("Initialized Log!");
	CR_INFO("Initialized Log!");

	auto app = Circuitizer::CreateApplication();
	app->Run();
	delete app;
}

#endif // CR_PLATFORM_WINDOWS
