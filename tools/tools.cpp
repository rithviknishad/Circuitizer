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
	math::polar p = { 2.0, 0.0 };
	math::polar q = math::polar().fromPolar(5, -piby2);

	math::complex a = { 1.0, 1.0 };
	q = a.getPolar();

	std::cout << "p = "; printPolar(p);
	std::cout << "q = "; printPolar(q);

	std::cout << "p * q = "; printPolar(q.conjugate());

	return 0;
}