#pragma once

#include "crpch.h"
#include "Circuitizer/Components/Component.h"

namespace Electrical
{
	class CIRCUITIZER_API Resistor : public Component
	{
	public:
		Resistor(double resistance = 1.0, std::string name = "") 
			: Component("Resistor"), m_Resistance(resistance)
		{ 
			AddTerminals(2);
		}
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
	
		virtual void OnUpdate(double time)
		{
			Component::OnUpdate(time);
		}

	protected:
		/* Resistance (unit: Ohms) */
		double m_Resistance = 0.0;
	};
}