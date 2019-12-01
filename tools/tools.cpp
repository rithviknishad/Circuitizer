// tools.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "math/complex.h"

void printPolar(math::polar polar)
{
	std::cout << "{" << polar.abs << ", " << PHI << " = " << polar.phi_d / pi << PI << "}" << std::endl;
}

int main()
{
	math::complex p = { 2.0, 0.0 };
	math::complex q = math::complex().fromRectangle(5, 3);

	std::cout << "start\n";

	for (double i = 0; i < 100000000; ++i)
	{
		math::complex a = p * q;
	}

	std::cout << "end\n";

	return 0;
}