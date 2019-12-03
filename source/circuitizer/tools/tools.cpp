// tools.cpp : Defines the entry point for the application.
//

#include "tools.h"

#include "angle.h"

void print(angle t)
{
	std::cout << t / pi << PI << std::endl;
}

int main()
{
	std::cout << "$ tools.exe has started" << std::endl;
	
	angle theta = piby2;

	print(theta);
	print(math::abs_rad(theta + pi2));
	print(atan2(8, 0));

	std::cin.get();
	return 0;
}
