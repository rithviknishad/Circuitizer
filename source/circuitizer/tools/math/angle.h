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

		angle& from_asin(const double value);
		angle& from_acos(const double value);
		angle& from_atan(const double value);
		angle& from_atan2(const double y, const double x);

		angle& operator+=(const angle& rhs);
		angle& operator-=(const angle& rhs);
		angle& operator*=(const double factor);
		angle& operator/=(const double factor);

		angle absolute();

		double sin() const;
		double cos() const;
		double tan() const;

		double sinh() const;
		double cosh() const;
		double tanh() const;
	} angle;

	angle operator+(const angle lhs, const angle rhs);
	angle operator-(const angle lhs, const angle rhs);
	angle operator-(const angle rhs);
	angle operator*(const angle lhs, const double factor);
	angle operator/(const angle lhs, const double factor);
	angle operator*(const double factor, const angle& lhs);

	double sin(const angle theta);
	double cos(const angle theta);
	double tan(const angle theta);

	double sinh(const angle theta);
	double cosh(const angle theta);
	double tanh(const angle theta);

	angle asin(const double x);
	angle acos(const double x);
	angle atan(const double x);

#pragma endregion
}

#include "angle.cpp"
#endif // !ANGLE_H
