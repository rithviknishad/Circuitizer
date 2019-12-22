#pragma once

#include "Circuitizer/Renderer/GraphicsContext.h"

struct GLFWwindow;

namespace Circuitizer
{
	class CIRCUITIZER_API OpenGLContext : public GraphicsContext
	{
	public:

		OpenGLContext(GLFWwindow* windowHandle);

		virtual void Init() override;
		virtual void SwapBuffers() override;

	private:
		GLFWwindow* m_WindowHandle;
	};
}