
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

		double projection();
		double projectionOn(polar base);

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
		complex(const double _real, const double _imaginary);
		complex(const struct polar p);
		complex(const double _abs, const angle _phi);
		
		complex& fromPolar(const struct polar p);
		complex& fromPolar(const double _abs, const double _phi_d);
		complex& fromPolar(const double _abs, const angle _phi);
		complex& fromRectangle(const double _r, const double _i);

		double norm();
		
		double absolute();
		double abs();
		
		angle argument();
		angle arg();
		angle phi();
		angle phase();

		struct polar polar();

		complex conjugate();

		double projection();
		double projectionOn(const complex base);
		double projectionOn(const struct polar base);

		complex& operator+=(const complex rhs);
		complex& operator-=(const complex rhs);
		complex& operator*=(const complex rhs);
		complex& operator/=(const complex rhs);

	} complex;

	complex operator+(const complex lhs, const complex rhs);
	complex operator-(const complex lhs, const complex rhs);
	complex operator*(const complex lhs, const complex rhs);
	complex operator/(const complex lhs, const complex rhs);

#pragma endregion

}

#include "complex.cpp"

#endif // !COMPLEX_H