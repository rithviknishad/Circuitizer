#pragma once

#include "crpch.h"
#include "Circuitizer/Components/Component.h"
#include "Circuitizer/Circuit/Types.h"

namespace Circuitizer
{
	class Resistor : public Component
	{
	public:

		Resistor(double p_resistance, std::string name = "Resistor", Position position = Origin)
			: Component(name, 2, position), R(p_resistance)
		{
		}

		/* Returns the voltage drop (unit: V) across the resistor. */
		inline V VDrop() { return m_Terminals[0]->Voltage - m_Terminals[1]->Voltage; }
		
		/* Returns the current (unit: A) passing through the resistor. */
		inline I Current() { return VDrop() / R; }

		R R;
	};
}