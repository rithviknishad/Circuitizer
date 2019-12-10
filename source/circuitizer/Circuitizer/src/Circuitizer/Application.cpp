#include "crpch.h"

#include "Application.h"

#include "Circuitizer/Events/ApplicationEvent.h"
#include "Circuitizer/Log.h"

namespace Circuitizer
{
	Application::Application()
	{
	}

	Application::~Application()
	{
	}

	void Application::Run()
	{
		WindowResizeEvent e(1280, 720);

		if (e.IsInCategory(EventCategoryApplication))
		{
			CR_TRACE(e);
		}
		if (e.IsInCategory(EventCategoryInput))
		{
			CR_TRACE(e);
		}

		while (true);
	}
}