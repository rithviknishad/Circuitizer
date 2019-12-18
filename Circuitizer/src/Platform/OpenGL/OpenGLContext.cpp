#include "crpch.h"
#include "OpenGLContext.h"

#include <GLFW/glfw3.h>
#include <glad/glad.h>

namespace Circuitizer
{
	
	OpenGLContext::OpenGLContext(GLFWwindow* windowHandle)
		: m_WindowHandle(windowHandle)
	{
		CR_CORE_ASSERT(windowHandle, "Window Handle is null");
	}

	void OpenGLContext::Init()
	{
		glfwMakeContextCurrent(m_WindowHandle);
		int status = gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);
		CR_CORE_ASSERT(status, "Failed to initialize Glad!");
		
		CR_CORE_INFO("OpenGL Info:");
		CR_CORE_INFO("  Vendor: {0}", glGetString(GL_VENDOR));
		CR_CORE_INFO("  Renderer: {0}", glGetString(GL_RENDERER));
		CR_CORE_INFO("  Version: {0}", glGetString(GL_VERSION));

	}

	void OpenGLContext::SwapBuffers()
	{
		glfwSwapBuffers(m_WindowHandle);
	}
}