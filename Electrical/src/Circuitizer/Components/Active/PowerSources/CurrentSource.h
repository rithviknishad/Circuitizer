#pragma once

#include "crpch.h"
#include "Circuitizer/Components/Component.h"
#include "Circuitizer/Components/Passive/Resistor.h"
#include "Circuitizer/Components/Active/PowerSources/VoltageSource.h"

namespace Circuitizer
{
	class CurrentSource : protected VoltageSource
	{
	public:
		CurrentSource(double current = 0.0, std::string name = "", double internalResistance = INFINITY)
		{
		}

	private:
		double m_Current;

		Resistor* m_InternalResistor;

		Terminal* OutTerminal;
		Terminal* InTerminal;
	};
}