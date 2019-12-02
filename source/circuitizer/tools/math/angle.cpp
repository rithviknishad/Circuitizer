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

angle& math::angle::from_asin(const double x)
{
	rad = std::asin(x);
	return *this;
}

angle& math::angle::from_acos(const double x)
{
	rad = std::acos(x);
	return *this;
}

angle& math::angle::from_atan(const double x)
{
	rad = std::atan(x);
	return *this;
}

angle& math::angle::from_atan2(const double y, const double x)
{
	rad = std::atan2(y, x);
	return *this;
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

double math::angle::sin() const
{
	return std::sin(rad);
}

double math::angle::cos() const
{
	return std::cos(rad);
}

double math::angle::tan() const
{
	return std::tan(rad);
}

double math::angle::sinh() const
{
	return std::sinh(rad);
}

double math::angle::cosh() const
{
	return std::cosh(rad);
}

double math::angle::tanh() const
{
	return std::tanh(rad);
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

double math::sin(const angle theta)
{
	return theta.sin();
}

double math::cos(const angle theta)
{
	return theta.cos();
}

double math::tan(const angle theta)
{
	return theta.tan();
}

double math::sinh(const angle theta)
{
	return theta.sinh();
}

double math::cosh(const angle theta)
{
	return theta.cosh();
}

double math::tanh(const angle theta)
{
	return theta.tanh();
}

angle math::asin(const double x)
{
	return angle().from_asin(x);
}

angle math::acos(const double x)
{
	return angle().from_acos(x);
}

angle math::atan(const double x)
{
	return angle().from_atan(x);
}


#pragma endregion