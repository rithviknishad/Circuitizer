// tools.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "edef/power.h"
#include "math/complex.h"

void printPolar(math::polar polar)
{
	std::cout << "{" << polar.abs << ", " << PHI << " = " << polar.phi_d / pi << PI << "}" << std::endl;
}

void printPower(e::power pwr)
{
	std::cout << "{" << pwr.value.abs() << " = " << pwr.P << " j" << pwr.Q << "}" << std::endl;
}

int main()
{
	e::power p = e::power().fromComplex(10, 20);
	printPower(p);

	double a = 0.0;

	std::cout << std::acos(10.0);

	//std::cout << math::acos(math::cos(math::asin(math::sin(angle().from_atan2(0.0, 8.0))))).rad / pi << PI;
	return 0;
}