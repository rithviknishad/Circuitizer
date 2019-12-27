#pragma once

#include "Circuitizer/Math/Math.h"

namespace Circuitizer
{
	using namespace Math;

	typedef class Resistance : public Numeric
	{
	public:
		Resistance(std::pair<double, double> value) : Numeric(value) {}
		Resistance(double value) : Numeric(value) {}
		Resistance(double real, double imaginary) : Numeric(real, imaginary) {}
		Resistance(Complex& c) : Numeric(c) {}

		Resistance& operator= (double value) { Numeric(value); return *this; }
	};
}