#pragma once

namespace Circuitizer
{
	class CIRCUITIZER_API GraphicsContext
	{
	public:
		virtual void Init() = 0;
		virtual void SwapBuffers() = 0;

	private:

	};
}