#pragma once

#include "crpch.h"

#include "Circuitizer/Components/Component.h"
#include "Circuitizer/Components/Passive/Resistor.h"

namespace Electrical
{
	/*
	==============================================================
	Components > Active > Power Sources > VOLTAGE SOURCE
	==============================================================

	Represents a voltage source with internal resistance.
	Contains two public terminals, and one shared private terminal.

	===============================================================
	
	Voltage Source Structure ( PUBLIC ):
		- VTerminal[0]	<--- OC. V --->	VTerminal[1]
	----------------

	Voltage Source (internal):	
		- VTerminal[0]	<--- Set V --->	RTerminal[0], aka
		- VTerminal[0]	<--- Set V --->	iVTerminal
	----------------

	Internal Resistance (internal): 
		- RTerminal[0]	<--- Int R --->	RTerminal[1], aka
		- RTerminal[0]	<--- Int R --->	VTerminal[1].
	----------------
	
	Terminal Sharing:
		- VTerminal[0];
		- iVTerminal, RTerminal[0];
		- VTerminal[1], RTerminal[1];

	===============================================================
	*/


	/*
	Voltage source
	*/
	class VoltageSource : public Component
	{
	public:
		
		VoltageSource(double voltage = 0.0, std::string name = "<unnamed>", double internalResistance = 0.0)
			: Component(name), m_Voltage(voltage), m_InternalResistor(new Resistor(internalResistance, name + "_InternalResistor"))
		{
			m_NegativeTerminal = new Terminal(name + "_PositiveTerminal");
			
			m_PositiveTerminal = m_InternalResistor->GetTerminals()[1];
			m_PositiveTerminal->SetName(name + "_NegativeTerminal");

			AddTerminal(m_NegativeTerminal);
			AddTerminal(m_PositiveTerminal);

			m_sharedTerminal = m_InternalResistor->GetTerminals()[0];
			m_sharedTerminal->SetName(name + "_internalSharedTerminal");
		}

		~VoltageSource() {}

		/* Sets the name of the Voltage Source. */
		virtual void SetName(std::string name) override
		{ 
			Component::SetName(name);
			m_InternalResistor->SetName(name + "_InternalResistor");
		}

		/* Sets the Open Circuit Voltage value of the component. */
		inline virtual void SetVoltage(double v_diff)
		{ 
			m_sharedTerminal->Voltage = m_NegativeTerminal->Voltage + (m_Voltage = v_diff);
		}

		/* Sets the resistance of the internal resistor. */
		inline virtual void SetInternalResistance(double value) { m_InternalResistor->SetResistance(value); }

		/* Returns  the output voltage across the terminals of the component. */
		inline double Voltage() { return m_PositiveTerminal->Voltage - m_NegativeTerminal->Voltage; }

		/* Returns the voltage drop across the internal resistor in the voltage source. */
		inline double VoltageDrop() { return m_PositiveTerminal->Voltage - m_sharedTerminal->Voltage; }

		inline Terminal* PositiveTerminal() { return m_PositiveTerminal; }
		inline Terminal* NegativeTerminal() { return m_NegativeTerminal; }

	protected:
		double m_Voltage = 0.0;
		
		Resistor* m_InternalResistor;

		Terminal* m_NegativeTerminal;
		Terminal* m_PositiveTerminal;
		Terminal* m_sharedTerminal;
	};
}