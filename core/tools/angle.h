#pragma once

#include "emath.h"

namespace math
{
	typedef struct angle
	{
		union { double radian, value, rad; };

		angle();
		angle(double val);
		angle(angle &obj);

		operator double();
		operator float();

		angle& absolute();

		angle& operator=(const angle rhs);

		angle& operator+=(const angle rhs);
		angle& operator-=(const angle rhs);

		angle& operator+=(const double rhs);
		angle& operator-=(const double rhs);

	} angle;

	angle absolute(const angle rhs);

	angle operator+(const angle lhs, const angle rhs);
	angle operator+(const angle lhs, const double rhs);
	angle operator-(const angle lhs);
	angle operator-(const angle lhs, const angle rhs);
	angle operator-(const angle lhs, const double rhs);
}