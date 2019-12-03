#ifndef POWER_H
#define POWER_H

#include "../math/complex.h"

using namespace math;

namespace e
{
	typedef struct power
	{
		union
		{
			union
			{
				complex value, apparentPower, S, A;
			};
			struct
			{
				union
				{
					double truePower, P, x, real;
				};
				union
				{
					double reactivePower, Q, y, imaginary;
				};

			};
		};


		power();
		power(complex c);
		power(const double p, const double q);
		power(polar p);
		power(const double _abs, const angle _phi);

		power& fromComplex(const complex c);
		power& fromComplex(const double p, const double q);
		power& fromPolar(const polar p);

		power& fromPolar(const double _abs, const double _phi_d);
		power& fromPolar(const double _abs, const angle _phi);

	} power;

#include "power.cpp"
}

#endif // !POWER_H