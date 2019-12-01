
#ifndef COMPLEX_H
#define COMPLEX_H

namespace math
{

#define PI 3.14159265358979
#define PI2 6.2831853071795
#define PIby2 1.5707963267949
#define PI3by2 4.71238898038468

#pragma region Angle

	typedef struct angle
	{
		double value;

		angle();
		angle(const double radian);

		angle& operator+=(const angle& rhs);
		angle& operator-=(const angle& rhs);
		angle& operator*=(const double factor);
		angle& operator/=(const double factor);

		angle absolute();
	} angle;

	angle operator+(const angle lhs, const angle rhs);
	angle operator-(const angle lhs, const angle rhs);
	angle operator*(const angle lhs, const double factor);
	angle operator/(const angle lhs, const double factor);
	angle operator*(const double factor, const angle& lhs);

#pragma endregion

#pragma region polar

	typedef struct polar
	{
		union { double absolute, magnitude, abs, mag; };
		union
		{
			angle phase, theta, arg, phi;
			double phi_d, theta_d, arg_d;
		};

		polar();
		polar(const double _absolute, const double phase_angle);

		polar& fromPolar(const double _absolute, const angle _phase);
		polar& fromRectangle(const double r, const double i);

		double real() const;
		double imaginary() const ;
		double norm() const;
		polar& conjugate() const;


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

}

#include "complex.cpp"

#endif // !COMPLEX_H