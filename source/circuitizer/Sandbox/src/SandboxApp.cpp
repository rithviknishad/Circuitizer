#include <Circuitizer.h>

class ExampleLayer : public Circuitizer::Layer
{
public:
	ExampleLayer() : Layer("Example")
	{
	}

	void OnUpdate() override
	{
		CR_INFO("ExampleLayer::Update");
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
		PushLayer(new Circuitizer::ImGuiLayer());
	}

	~Sandbox()
	{
	}


};

Circuitizer::Application* Circuitizer::CreateApplication()
{
	return new Sandbox();
}