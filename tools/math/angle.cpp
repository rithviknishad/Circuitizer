#include "angle.h"

#include "math.h"

using namespace math;

#pragma region Angle

angle::angle()
{
	value = 0.0;
}

angle::angle(const double rad)
{
	value = rad;
	absolute();
}


angle& angle::operator+=(const angle& rhs)
{
	value += rhs.value;
	return *this;
}

angle& angle::operator-=(const angle& rhs)
{
	value -= rhs.value;
	return *this;
}

angle& angle::operator*=(const double factor)
{
	value *= factor;
	return *this;
}

angle& angle::operator/=(const double factor)
{
	value /= factor;
	return *this;
}

angle angle::absolute()
{
	if (value < 0.0)
		value += ((int)(-value / pi2) + 1.0) * pi2;
	else if (value >= pi2)
		value -= ((int)(value / pi2)) * pi2;

	return *this;
}


angle math::operator+(const angle lhs, const angle rhs)
{
	return angle(lhs.value + rhs.value);
}

angle math::operator-(const angle lhs, const angle rhs)
{
	return angle(lhs.value - rhs.value);
}

angle math::operator-(const angle rhs)
{
	return angle(-rhs.value).absolute();
}

angle math::operator*(const angle lhs, const double factor)
{
	return angle(lhs.value * factor);
}

angle math::operator/(const angle lhs, const double factor)
{
	return angle(lhs.value / (factor == 0.0 ? 1 : factor));
}

angle math::operator*(const double factor, const angle& lhs)
{
	return angle(lhs.value * factor);
}

#pragma endregion