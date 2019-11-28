
#include "complex.h"
#include <string>

using namespace math;



math::angle::angle()
{
	value = 0.0;
}

math::angle::angle(double val)
{
	value = 0.0;
}

angle& math::angle::operator+=(const angle& rhs)
{
	value += rhs.value;
	return *this;
}

angle& math::angle::operator-=(const angle& rhs)
{
	value -= rhs.value;
	return *this;
}

angle& math::angle::operator*=(const double factor)
{
	value *= factor;
	return *this;
}

angle& math::angle::operator/=(const double factor)
{
	value /= factor;
	return *this;
}

angle& math::angle::makeabsolute()
{
	// TODO: insert return statement here
}

angle& math::operator+(const angle& lhs, const angle& rhs)
{
	return angle(lhs.value + rhs.value);
}

angle& math::operator-(const angle& lhs, const angle& rhs)
{
	return angle(lhs.value - rhs.value);
}

angle& math::operator*(const angle& lhs, const double factor)
{
	return angle(lhs.value * factor);
}

angle& math::operator/(const angle& lhs, const double factor)
{
	return angle(lhs.value / factor);
}

angle& math::operator*(const double factor, const angle& lhs)
{
	return angle * factor;
}

angle& math::operator/(const double factor, const angle& lhs)
{
	return angle / factor;
}
