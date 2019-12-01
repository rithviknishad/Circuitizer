
#ifndef COMPLEX_H
#define COMPLEX_H

namespace math
{

// MATHEMATICAL CONSTANTS
#define pi 3.14159265358979
#define pi2 6.2831853071795
#define piby2 1.5707963267949
#define pi3by2 4.71238898038468

// MATHEMATICAL SYMBOLS
#define PHI char(237)
#define PI char(227)

#pragma region Angle

	typedef struct angle
	{
		union
		{
			double value, rad, radian;
		};

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
	angle operator-(const angle rhs);
	angle operator*(const angle lhs, const double factor);
	angle operator/(const angle lhs, const double factor);
	angle operator*(const double factor, const angle& lhs);

#pragma endregion

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