#include <iostream>

#include "tools/angle.h"

int main()
{
	std::cout << "$ Core Initiated" << std::endl;

	math::angle a = 3.6;
	a = -a;
	std::cout << (double)a << std::endl;

	std::cin.get();
	return 0;
}