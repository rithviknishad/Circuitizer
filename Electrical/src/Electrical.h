#pragma once

void PutAutoBreakPointsForDiagnostics();

// For use by Circuitizer Applications

#include "Circuitizer/Components/Resistor.h"

using namespace Electrical;

void CircuitizerTestingLab_EntryPoint()
{
	PutAutoBreakPointsForDiagnostics();

	Resistor* resistor = new Resistor();

	double v = resistor->VoltageDrop();
	double i = resistor->Current();

	delete resistor;
}