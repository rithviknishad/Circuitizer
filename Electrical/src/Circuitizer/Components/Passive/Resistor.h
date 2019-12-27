#pragma once

#include "crpch.h"
#include "Circuitizer/Components/Component.h"
#include "Circuitizer/Circuit/Resistance.h"

namespace Circuitizer
{
	class Resistor : public Component, public 
	{
	public:
		Resistor(double resistance, std::string name = "Resistor", Position position = Origin) : Component(name, 2, position), m_Resistance(resistance) {}

		~Resistor()
		{
			for (Terminal* terminal : m_Terminals)
				delete terminal;
		}

		/* Returns the resistance of resistor (unit: Ohms) */
		inline double Resistance() { return m_Resistance; }
		
		/* Sets the resistance of the resistor (unit: Ohms) */
		inline void SetResistance(double resistance) { m_Resistance = resistance; }

		/* Returns the voltage drop (unit: V) across the resistor. */
		inline double VoltageDrop() { return m_Terminals[0]->Voltage - m_Terminals[1]->Voltage; }

		/* Returns the current (unit: A) passing through the resistor. */
		inline double Current() { return VoltageDrop() / m_Resistance; }

	protected:
		/* Resistance (unit: Ohms) */
		double m_Resistance = 0.0;
	};
}