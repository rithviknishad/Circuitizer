#pragma once

#include "Core.h"

namespace Circuitizer
{

	class CIRCUITIZER_API Application
	{
	public:
		Application();
		virtual ~Application();

		void Run();
	};

	// To be defined in client
	Application* CreateApplication();

}