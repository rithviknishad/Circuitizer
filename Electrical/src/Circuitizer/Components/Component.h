#pragma once

#include "crpch.h"
#include "Circuitizer/Generic/Generics.h"
#include "Circuitizer/Circuit/TerminalContainer.h"

namespace Circuitizer
{
	class Component : public Name, public Position, public TerminalContainer
	{
	public:
		Component(std::string name, int pinCount, Position position)
			: Name(name), Position(position)
		{
			AddTerminals(pinCount, name);
		}
	};
}