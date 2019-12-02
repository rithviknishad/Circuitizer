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

math::complex::complex(const double _real, const double _imaginary)
{
	fromRectangle(_real, _imaginary);
}

math::complex::complex(struct polar p)
{
	fromPolar(p);
}

math::complex::complex(const double _abs, const angle _phi)
{
	fromPolar(_abs, _phi);
}

complex& math::complex::fromPolar(const struct polar p)
{
	real = p.real();
	imaginary = p.imaginary();
	return *this;
}

complex& math::complex::fromPolar(const double _abs, const double _phi_d)
{
	r = _abs * std::cos(_phi_d);
	i = _abs * std::sin(_phi_d);
	return *this;
}

complex& math::complex::fromPolar(const double _abs, const angle _phi)
{
	fromPolar(_abs, _phi.rad);
	return *this;
}

complex& math::complex::fromRectangle(const double _r, const double _i)
{
	real = _r;
	imaginary = _i;
	return *this;
}

double math::complex::norm() const
{
	return ((x * x) + (y * y));
}

double math::complex::absolute() const
{
	return std::sqrt(norm());
}

double math::complex::abs() const
{
	return std::sqrt(norm());
}

angle math::complex::argument() const
{
	return angle(std::atan2(i, r)).absolute();
}

angle math::complex::arg() const
{
	return angle(std::atan2(i, r)).absolute();
}

angle math::complex::phi() const
{
	return angle(std::atan2(i, r)).absolute();
}

angle math::complex::phase() const
{
	return angle(std::atan2(i, r)).absolute();
}

struct polar math::complex::polar() const
{
	return struct polar().fromRectangle(r, i);
}

complex math::complex::conjugate() const
{
	return complex().fromRectangle(real, -imaginary);
}

double math::complex::projection() const
{
	return x;
}

double math::complex::projectionOn(const complex base) const
{
	return complex::polar().projectionOn(polar().fromRectangle(base.r, base.i));
}

double math::complex::projectionOn(const struct polar base) const
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

complex& math::complex::operator+=(const polar rhs)
{
	r += rhs.real();
	i += rhs.imaginary();
	return *this;
}

complex& math::complex::operator-=(const polar rhs)
{
	r -= rhs.real();
	i -= rhs.imaginary();
	return *this;
}

complex&  math::complex::operator*=(const polar rhs)
{
	return (*this) *= complex(rhs);
}

complex& math::complex::operator /=(const polar rhs)
{
	return (*this) /= complex(rhs);
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

complex math::operator+(const polar lhs, const complex rhs)
{
	return complex(lhs) + rhs;
}

complex math::operator-(const polar lhs, const complex rhs)
{
	return complex(lhs) - rhs;
}

complex math::operator*(const polar lhs, const complex rhs)
{
	return complex(lhs) * rhs;
}

complex math::operator/(const polar lhs, const complex rhs)
{
	return complex(lhs) / rhs;
}

complex math::operator+(const complex lhs, const polar rhs)
{
	return lhs + complex(rhs);
}

complex math::operator-(const complex lhs, const polar rhs)
{
	return lhs - complex(rhs);
}

complex math::operator*(const complex lhs, const polar rhs)
{
	return lhs * complex(rhs);
}

complex math::operator/(const complex lhs, const polar rhs)
{
	return lhs / complex(rhs);
}

#pragma endregion