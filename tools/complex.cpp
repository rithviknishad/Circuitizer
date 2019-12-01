#include <cmath>
#include "complex.h"

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
		value += ((int)(-value / PI2) + 1.0) * PI2;
	else if (value >= PI2)
		value -= ((int)(value / PI2)) * PI2;

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

//#pragma region complex
//
//::complex::complex()
//{
//	r = i = 0;
//}
//
//::complex::complex(const double _r, const double _i)
//{
//	r = _r;
//	i = _i;
//}
//
//::complex::complex(const double mag, const angle dir)
//{
//	r = mag * cos(dir.value);
//	i = mag * sin(dir.value);
//}
//
//complex& complex::operator+=(const complex& rhs)
//{
//	r += rhs.r;
//	i = rhs.i;
//}
//
//complex& complex::operator-=(const complex& rhs)
//{
//	r -= rhs.r;
//	i -= rhs.i;
//}
//
//complex& complex::operator*=(const complex& rhs)
//{
//	r = (r * rhs.r) - (i * rhs.i);
//	i = (r * rhs.i) + (i * rhs.r);
//}
//
//complex& complex::operator/=(const complex& rhs)
//{
//	r = ((r * rhs.r) + (i * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i));
//	i = ((i * rhs.r) - (r * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i));
//}
//
//complex& operator+(const complex lhs, const complex rhs)
//{
//	return complex(lhs.r + rhs.r, lhs.i + rhs.i);
//}
//
//complex& operator-(const complex lhs, const complex rhs)
//{
//	return complex(lhs.r - rhs.r, lhs.i - rhs.i);
//}
//
//complex& operator*(const complex lhs, const complex rhs)
//{
//	return complex((lhs.r * rhs.r) - (lhs.i * rhs.i), (lhs.r * rhs.i) + (lhs.i * rhs.r));
//}
//
//complex& operator/(const complex lhs, const complex rhs)
//{
//	return complex(((lhs.r * rhs.r) + (lhs.i * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i)), ((lhs.i * rhs.r) - (lhs.r * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i)));
//}
//
//#pragma endregion

#pragma region polar

math::polar::polar()
{
	phase = angle();
	abs = theta_d = 0.0;
}

math::polar::polar(const double _absolute, const double phase_angle)
{
	abs = _absolute;
	phase = angle(phase_angle).absolute();
}

polar& polar::fromPolar(const double _absolute, const angle _phase)
{
	abs = _absolute;
	phi.value = _phase.value;
	return *this;
}

polar& polar::fromRectangle(const double r, const double i)
{
	abs = std::sqrt((r * r) + (i * i));
	phase = angle(std::atan2(i, r));
	return *this;
}

double polar::real() const
{
	return abs * std::cos(phi_d);
}

double polar::imaginary() const 
{
	return abs * std::sin(phi_d);
}

double polar::norm() const 
{
	return abs * abs;
}

polar& polar::conjugate() const 
{
	return (polar().fromRectangle(real(), -imaginary()));
}



polar& math::polar::operator+=(const polar rhs)
{
	fromRectangle(real() + rhs.real(), imaginary() + rhs.imaginary());
	return *this;
}

polar& math::polar::operator-=(const polar rhs)
{
	fromRectangle(real() - rhs.real(), imaginary() - rhs.imaginary());
	return *this;
}

polar& math::polar::operator*=(const polar rhs)
{
	fromPolar(abs * rhs.abs, phi + rhs.phi);
	return *this;
}

polar& math::polar::operator/=(const polar rhs)
{
	fromPolar(abs / rhs.abs, phi - rhs.phi);
	return *this;
}

polar math::operator+(const polar lhs, const polar rhs)
{
	return polar().fromRectangle(lhs.real() + rhs.real(), lhs.imaginary() + rhs.imaginary());
}

polar math::operator-(const polar lhs, const polar rhs)
{
	return polar().fromRectangle(lhs.real() - rhs.real(), lhs.imaginary() - rhs.imaginary());
}

polar math::operator*(const polar lhs, const polar rhs)
{
	return polar().fromPolar(lhs.abs * rhs.abs, lhs.phi + rhs.phi);
}

polar math::operator/(const polar lhs, const polar rhs)
{
	return polar().fromPolar(lhs.abs / rhs.abs, lhs.phi - rhs.phi);
}

#pragma endregion