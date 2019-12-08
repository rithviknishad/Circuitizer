#pragma once
#include "angle.h"

using namespace math;

math::angle::angle()
{
	radian = 0.0;
}

math::angle::angle(double val)
{
	radian = val;
	absolute();
}

math::angle::angle(angle& obj)
{
	radian = obj.radian;
	absolute();
}

math::angle::operator double()
{
	absolute();
	return radian;
}

math::angle::operator float()
{
	absolute();
	return (float)radian;
}

angle& math::angle::absolute()
{
	if (radian < 0.0)
		radian += (((int)(-radian / pi2)) + 1.00) * pi2;
	else if (radian >= pi2)
		radian -= ((int)(radian / pi2)) * pi2;

	return *this;
}

angle& math::angle::operator=(const angle rhs)
{
	radian = rhs.radian;
	return absolute();
}

angle& math::angle::operator+=(const angle rhs)
{
	radian += rhs.radian;
	return absolute();
}

angle& math::angle::operator-=(const angle rhs)
{
	radian -= rhs.radian;
	return absolute();
}

angle& math::angle::operator+=(const double rhs)
{
	radian += rhs;
	return absolute();
}

angle& math::angle::operator-=(const double rhs)
{
	radian -= rhs;
	return absolute();
}

angle math::absolute(const angle rhs)
{
	return angle(rhs.radian);
}

angle math::operator+(const angle lhs, const angle rhs)
{
	return angle(lhs.radian + rhs.radian);
}

angle math::operator+(const angle lhs, const double rhs)
{
	return angle(lhs.radian + rhs);
}

angle math::operator-(const angle lhs)
{
	return angle(-lhs.radian);
}

angle math::operator-(const angle lhs, const angle rhs)
{
	return angle(lhs.radian - rhs.radian);
}

angle math::operator-(const angle lhs, const double rhs)
{
	return angle(lhs.radian - rhs);
}
