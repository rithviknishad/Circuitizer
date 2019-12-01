// tools.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "complex.h"

void printPolar(math::polar polar)
{
	std::cout << polar.abs << " <" << polar.phi_d << std::endl;
}

int main()
{
	math::polar p = math::polar().fromPolar(10, 1);
	math::polar q = math::polar().fromPolar(5, 2);

	std::cout << "p = "; printPolar(p);
	std::cout << "q = "; printPolar(q);

	std::cout << "p * q = "; printPolar(p * q);

	return 0;
}
