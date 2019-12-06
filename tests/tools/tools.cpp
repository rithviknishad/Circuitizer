// tools.cpp : Defines the entry point for the application.
//

#include "tools.h"

#include "complex.cpp"

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
	
	using namespace math;

	for (double i = 0; i < pi2; i += pi2 / 360)
	{
		complex c = { cos(i), sin(i) };
		polar p = polar(c);
		print(conj(c));
		std::cout << "\t";
		print(conj(p));
		std::cout << "\n";
	}


	std::cin.get();
	return 0;
}