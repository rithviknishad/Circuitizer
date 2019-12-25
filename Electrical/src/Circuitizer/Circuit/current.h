#pragma once

#include "Circuitizer/Math/Math.h"

namespace Circuitizer
{
	using namespace math;

	typedef class Current : public Numeric
	{
	public:
        Current(std::pair<double, double> value) : Numeric(value) {}
        Current(double real = 0.0, double imaginary = 0.0) : Numeric(real, imaginary) {}
        Current(Complex& c) : Numeric(c) {}
	};
}