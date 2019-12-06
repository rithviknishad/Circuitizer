// tools.cpp : Defines the entry point for the application.
//

#include "tools.h"
#include "complex.h"

using namespace math;

void print(angle t)
{
	std::cout << t / pi << PI << std::endl;
}

void print(complex c)
{
	std::cout << c.real << " + " << c.imaginary << "i";
}

void print(polar p)
{
	std::cout << p.abs << " " << PHI << "=" << p.phi / pi << PI;
}

int main()
{
	std::cout << "$ tools.exe has started" << std::endl;

	complex a = complex(1, pi);
	complex b = complex(2, piby2);

	for (double i = 0; i < 100000000; i ++)
	{
		complex c = complex(polar(complex(a + b)));
	}

	std::cout << "Finsihed";

	std::cin.get();
	return 0;
}