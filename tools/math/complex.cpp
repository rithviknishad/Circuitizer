#include "complex.h"

#include <cmath>
#include "angle.h"

using namespace math;

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

math::polar::polar(const double _absolute, const angle phase_angle)
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
	phase = angle(std::atan2(i, r)).absolute();
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

polar polar::conjugate() const 
{
	return polar(abs, -phi);
}

double math::polar::projection()
{
	return real();
}

double math::polar::projectionOn(polar base)
{
	return polar().fromPolar(abs, phi.absolute() - base.phi.absolute()).real();
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

#pragma region complex

math::complex::complex()
{
	fromRectangle(0.0, 0.0);
}

math::complex::complex(double _real, double _imaginary)
{
	fromRectangle(_real, _imaginary);
}

complex& math::complex::fromPolar(const polar p)
{
	real = p.real();
	imaginary = p.imaginary();
	return *this;
}

complex& math::complex::fromRectangle(const double _r, const double _i)
{
	real = _r;
	imaginary = _i;
	return *this;
}

double math::complex::norm()
{
	return ((x * x) + (y * y));
}

double math::complex::absolute()
{
	return std::sqrt(norm());
}

double math::complex::abs()
{
	return std::sqrt(norm());
}

angle math::complex::argument()
{
	return angle(std::atan2(i, r)).absolute();
}

angle math::complex::arg()
{
	return angle(std::atan2(i, r)).absolute();
}

angle math::complex::phi()
{
	return angle(std::atan2(i, r)).absolute();
}

angle math::complex::phase()
{
	return angle(std::atan2(i, r)).absolute();
}

polar& math::complex::polar()
{
	return struct polar(abs, phi);
}

complex math::complex::conjugate()
{
	return complex().fromRectangle(real, -imaginary);
}

double math::complex::projection()
{
	return x;
}

double math::complex::projectionOn(const complex base)
{
	return complex::polar().projectionOn(polar().fromRectangle(base.r, base.i));
}

double math::complex::projectionOn(const polar base)
{
	return complex::polar().projectionOn(base);
}

complex& math::complex::operator+=(const complex rhs)
{
	real += rhs.real;
	imaginary += rhs.imaginary;
	return *this;
}

complex& math::complex::operator-=(const complex rhs)
{
	real -= rhs.real;
	imaginary -= rhs.imaginary;
	return *this;
}

complex& math::complex::operator*=(const complex rhs)
{
	r = (r * rhs.r) - (i * rhs.i);
	i = (r * rhs.i) + (i * rhs.r);
	return *this;
}

complex& math::complex::operator/=(const complex rhs)
{
	r = ((r * rhs.r) + (i * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i));
	i = ((i * rhs.r) - (r * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i));
	return *this;
}

complex math::operator+(const complex lhs, const complex rhs)
{
	return complex(lhs.r + rhs.r, lhs.i + rhs.i);
}

complex math::operator-(const complex lhs, const complex rhs)
{
	return complex(lhs.r - rhs.r, lhs.i - rhs.i);
}

complex math::operator*(const complex lhs, const complex rhs)
{
	return complex((lhs.r * rhs.r) - (lhs.i * rhs.i), (lhs.r * rhs.i) + (lhs.i * rhs.r));
}

complex math::operator/(const complex lhs, const complex rhs)
{
	return complex(((lhs.r * rhs.r) + (lhs.i * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i)), ((lhs.i * rhs.r) - (lhs.r * rhs.i)) / ((rhs.r * rhs.r) + (rhs.i * rhs.i)));
}

#pragma endregion