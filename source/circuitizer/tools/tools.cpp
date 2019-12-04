// tools.cpp : Defines the entry point for the application.
//

#include "tools.h"

#include "complex.h"

void print(angle t)
{
	std::cout << t / pi << PI << std::endl;
}

int main()
{
	std::cout << "$ tools.exe has started" << std::endl;
	
	using namespace math;

	complex a = { 1, 'c' };

	polar t = a;


	std::cin.get();
	return 0;
}
