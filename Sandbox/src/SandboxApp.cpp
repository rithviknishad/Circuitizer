#include <Circuitizer.h>

#include "imgui/imgui.h"

class ExampleLayer : public Circuitizer::Layer
{
public:
	ExampleLayer() : Layer("Example")
	{
	}

	void OnUpdate() override
	{
		//CR_INFO("ExampleLayer::Update");
	}

	void OnImGuiRender() override
	{
		/*ImGui::Begin("Test");
		ImGui::Text("Hello World");
		ImGui::End();*/
	}

	void OnEvent(Circuitizer::Event& event) override
	{
		CR_TRACE("{0}", event);
	}
};

class Sandbox : public Circuitizer::Application
{
public:
	Sandbox()
	{
		PushLayer(new ExampleLayer);
		//PushLayer(new Circuitizer::ImGuiLayer());
	}

	~Sandbox()
	{
	}


};

Circuitizer::Application* Circuitizer::CreateApplication()
{
	return new Sandbox();
}