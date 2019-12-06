#pragma once

#include "angle.h"

namespace math
{

	struct polar;
	struct complex;

	typedef struct polar
	{
		union { double abs, absolute; };
		union { angle phi, phase, arg; };

		polar(const double _abs = 0.0, const angle _phi = 0.0);
		polar(const complex c);

		polar& operator=(const polar rhs);

		polar& operator+=(const polar rhs);
		polar& operator-=(const polar rhs);
		polar& operator*=(const polar rhs);
		polar& operator/=(const polar rhs);

		/*polar& operator+=(const double rhs);
		polar& operator-=(const double rhs);
		polar& operator*=(const double rhs);
		polar& operator/=(const double rhs);

		polar& operator+=(const complex rhs);
		polar& operator-=(const complex rhs);
		polar& operator*=(const complex rhs);
		polar& operator/=(const complex rhs);*/

	} polar;

	typedef struct complex
	{
		union { double x, real, Re; };
		union { double y, imaginary, imag, Im; };

		complex(const double _real, const double _i);
		complex(const polar p);

		complex& operator=(const complex rhs);

		complex& operator+=(const complex rhs);
		complex& operator-=(const complex rhs);
		complex& operator*=(const complex rhs);
		complex& operator/=(const complex rhs);

		complex& operator+=(const double rhs);
		complex& operator-=(const double rhs);
		complex& operator*=(const double rhs);
		complex& operator/=(const double rhs);

		complex& operator+=(const polar rhs);
		complex& operator-=(const polar rhs);
		complex& operator*=(const polar rhs);
		complex& operator/=(const polar rhs);

	} complex;

	// operations

	complex operator+(const complex lhs, const complex rhs);
	complex operator-(const complex lhs);
	complex operator-(const complex lhs, const complex rhs);
	complex operator*(const complex lhs, const complex rhs);
	complex operator/(const complex lhs, const complex rhs);

	complex operator+(const complex lhs, const double rhs);
	complex operator-(const complex lhs, const double rhs);
	complex operator*(const complex lhs, const double rhs);
	complex operator/(const complex lhs, const double rhs);

	complex operator+(const double lhs, const complex rhs);
	complex operator-(const double lhs, const complex rhs);
	complex operator*(const double lhs, const complex rhs);
	complex operator/(const double lhs, const complex rhs);

	complex operator+(const complex lhs, const polar rhs);
	complex operator-(const complex lhs, const polar rhs);
	complex operator*(const complex lhs, const polar rhs);
	complex operator/(const complex lhs, const polar rhs);

	polar operator+(const polar lhs, const polar rhs);
	polar operator-(const polar lhs);
	polar operator-(const polar lhs, const polar rhs);
	polar operator*(const polar lhs, const polar rhs);
	polar operator/(const polar lhs, const polar rhs);

	/*polar operator+(const polar lhs, const double rhs);
	polar operator-(const polar lhs, const double rhs);
	polar operator*(const polar lhs, const double rhs);
	polar operator/(const polar lhs, const double rhs);

	polar operator+(const double lhs, const polar rhs);
	polar operator-(const double lhs, const polar rhs);
	polar operator*(const double lhs, const polar rhs);
	polar operator/(const double lhs, const polar rhs);

	polar operator+(const polar lhs, const complex rhs);
	polar operator-(const polar lhs, const complex rhs);
	polar operator*(const polar lhs, const complex rhs);
	polar operator/(const polar lhs, const complex rhs);*/


	// fuctions
	double real(const polar p);
	double real(const complex c);

	double imaginary(const polar p);
	double imaginary(const complex c);

	polar conj(const polar p);
	complex conj(const complex c);

	polar conjugate(const polar p);
	complex conjugate(const complex c);

	double projection(const polar p);
	double projection(const complex c);

	double norm(const polar p);
	double norm(const complex c);

	double abs(const polar p);
	double abs(const complex c);

	double absolute(const polar p);
	double absolute(const complex c);

	angle arg(const polar p);
	angle arg(const complex c);
	angle argument(const polar p);
	angle argument(const complex c);
	angle phi(const polar p);
	angle phi(const complex c);
	angle phase(const polar p);
	angle phase(const complex c);

}