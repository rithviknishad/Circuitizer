
#ifndef COMPLEX_H
#define COMPLEX_H

#include "angle.h"

namespace math
{
#pragma region polar

	typedef struct polar
	{
		union
		{ 
			double absolute, magnitude, abs, mag;
		};
		union
		{
			angle phase, theta, arg, phi;
			double phi_d, theta_d, arg_d;
		};

		polar();
		polar(const double _absolute, const double phase_angle);
		polar(const double _absolute, const angle phase_angle);

		polar& fromPolar(const double _absolute, const angle _phase);
		polar& fromRectangle(const double r, const double i);

		double real() const;
		double imaginary() const;
		double norm() const;
		polar conjugate() const;

		polar& operator+=(const polar rhs);
		polar& operator-=(const polar rhs);
		polar& operator*=(const polar rhs);
		polar& operator/=(const polar rhs);
	} polar;

	polar operator+(const polar lhs, const polar rhs);
	polar operator-(const polar lhs, const polar rhs);
	polar operator*(const polar lhs, const polar rhs);
	polar operator/(const polar lhs, const polar rhs);

#pragma endregion


#pragma region complex

	typedef struct complex
	{
		union
		{
			double real, r, x, p;
		};
		union
		{
			double imaginary, i, img, y, q;
		};

		complex();
		complex(double _real, double _imaginary);
		
		complex& fromPolar(const double _absolute, const angle _phase);
		complex& fromRectangle(const double _r, const double _i);

		polar& polar();



	} complex;

#pragma endregion


}

#include "complex.cpp"

#endif // !COMPLEX_H