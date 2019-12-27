#pragma once

#include "Circuitizer/Math/Math.h"

namespace Circuitizer
{
	using namespace Math;

	typedef class Voltage : public Numeric
	{
	public:		
		Voltage(std::pair<double, double> value) : Numeric(value) {}
		Voltage(double real = 0.0, double imaginary = 0.0) : Numeric(real, imaginary) {}
		Voltage(Complex& c) : Numeric(c) {}
	};
}