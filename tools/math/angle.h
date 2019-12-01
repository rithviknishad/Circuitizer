#ifndef ANGLE_H
#define ANGLE_H

namespace math
{
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
}

#include "angle.cpp"
#endif // !ANGLE_H
