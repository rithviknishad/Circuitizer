#pragma once

#include "Circuitizer/Layer.h"

#include "Circuitizer/Events/ApplicationEvent.h"
#include "Circuitizer/Events/KeyEvent.h"
#include "Circuitizer/Events/MouseEvent.h"

namespace Circuitizer
{
	class CIRCUITIZER_API ImGuiLayer : public Layer
	{
	public:
		ImGuiLayer();
		~ImGuiLayer();

		virtual void OnAttach() override;
		virtual void OnDetach() override;
		virtual void OnImGuiRender() override;

		void Begin();
		void End();

	private:
		float m_Time = 0.0f;
	};
}