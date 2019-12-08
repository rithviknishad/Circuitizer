#include <Circuitizer.h>

class Sandbox : public Circuitizer::Application
{
public:
	Sandbox()
	{
	}

	~Sandbox()
	{
	}


};

Circuitizer::Application* Circuitizer::CreateApplication()
{
	return new Sandbox();
}