#include "complex.h"

using namespace math;

math::polar::polar(const double _abs, const angle _phi)
{
	abs = _abs;
	phi = _phi;
}

math::polar::polar(const complex c)
{
	abs = math::abs(c);
	phi = math::arg(c);
}

polar& math::polar::operator=(const polar rhs)
{
	abs = rhs.abs;
	arg = rhs.arg;
	return *this;
}

polar& math::polar::operator+=(const polar rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator-=(const polar rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator*=(const polar rhs)
{
	abs *= rhs.abs;
	phi += rhs.phi;
	return *this;
}

polar& math::polar::operator/=(const polar rhs)
{
	abs /= rhs.abs;
	phi -= rhs.phi;
	return *this;
}

polar& math::polar::operator+=(const double rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator-=(const double rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator*=(const double rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator/=(const double rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator+=(const complex rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator-=(const complex rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator*=(const complex rhs)
{
	// TODO: insert return statement here
}

polar& math::polar::operator/=(const complex rhs)
{
	// TODO: insert return statement here
}

math::complex::complex(const double _real, const double _i)
{
	x = _real;
	y = _i;
}

math::complex::complex(const polar p)
{
	x = p.abs * cos(p.phi);
	y = p.abs * sin(p.phi);
}

complex& math::complex::operator=(const complex rhs)
{
	x = rhs.x;
	y = rhs.y;
	return *this;
}

complex& math::complex::operator+=(const complex rhs)
{
	x += rhs.x;
	y += rhs.y;
	return *this;
}

complex& math::complex::operator-=(const complex rhs)
{
	x -= rhs.x;
	y -= rhs.y;
	return *this;
}

complex& math::complex::operator*=(const complex rhs)
{
	const double _x = x;
	x = (_x * rhs.x) - (y * rhs.y);
	y = (_x * rhs.y) + (y * rhs.x);
	return *this;
}

complex& math::complex::operator/=(const complex rhs)
{
	const double d = (rhs.x * rhs.x) + (rhs.y * rhs.y), _x = x;
	x = ((_x * rhs.x) + (y * rhs.y)) / d;
	y = ((y * rhs.x) - (_x * rhs.y)) / d;
	return *this;
}

complex& math::complex::operator+=(const double rhs)
{
	x += rhs.x;
	return *this;
}

complex& math::complex::operator-=(const double rhs)
{
	x -= rhs.x;
	return *this;
}

complex& math::complex::operator*=(const double rhs)
{
	x *= rhs;
	y *= rhs;
	return *this;
}

complex& math::complex::operator/=(const double rhs)
{
	x /= rhs;
	y /= rhs;
	return *this;
}

complex& math::complex::operator+=(const polar rhs)
{
	// TODO: insert return statement here
}

complex& math::complex::operator-=(const polar rhs)
{
	// TODO: insert return statement here
}

complex& math::complex::operator*=(const polar rhs)
{
	// TODO: insert return statement here
}

complex& math::complex::operator/=(const polar rhs)
{
	// TODO: insert return statement here
}

complex math::operator+(const complex lhs, const complex rhs)
{
	return complex(lhs.x + rhs.x, lhs.y + rhs.y);
}

complex math::operator-(const complex lhs)
{
	return complex(-lhs.x, -lhs.y);
}

complex math::operator-(const complex lhs, const complex rhs)
{
	return lhs + (-rhs);
}

complex math::operator*(const complex lhs, const complex rhs)
{
	return complex((lhs.x * rhs.x) - (lhs.y * rhs.y), (lhs.x * rhs.y) + (lhs.y * rhs.x));
}

complex math::operator/(const complex lhs, const complex rhs)
{
	const double d = (rhs.x * rhs.x) + (rhs.y * rhs.y);
	return complex(((lhs.x * rhs.x) + (lhs.y * rhs.y)) / d, ((lhs.y * rhs.x) - (lhs.x * rhs.y)) / d);
}

complex math::operator+(const complex lhs, const double rhs)
{
	return complex(lhs.x + rhs.x, lhs.y);
}

complex math::operator-(const complex lhs, const double rhs)
{
	return complex(lhs.x - rhs.x, lhs.y);
}

complex math::operator*(const complex lhs, const double rhs)
{
	return complex(lhs.x * rhs, lhs.y * rhs);
}

complex math::operator/(const complex lhs, const double rhs)
{
	return complex(lhs.x / rhs, lhs.y / rhs);
}

complex math::operator+(const double lhs, const complex rhs)
{
	return complex(lhs + rhs.x, rhs.y);
}

complex math::operator-(const double lhs, const complex rhs)
{
	return complex(lhs - rhs.x, rhs.y);
}

complex math::operator*(const double lhs, const complex rhs)
{
	return complex(lhs * rhs.x, lhs * rhs.y);
}

complex math::operator/(const double lhs, const complex rhs)
{
	return complex(lhs / rhs.x, lhs / rhs.y);
}

complex math::operator+(const complex lhs, const polar rhs)
{
	return complex();
}

complex math::operator-(const complex lhs, const polar rhs)
{
	return complex();
}

complex math::operator*(const complex lhs, const polar rhs)
{
	return complex();
}

complex math::operator/(const complex lhs, const polar rhs)
{
	return complex();
}

polar math::operator+(const polar lhs, const polar rhs)
{
	return polar(complex(lhs) + complex(rhs));
}

polar math::operator-(const polar lhs)
{
	return polar();
}

polar math::operator-(const polar lhs, const polar rhs)
{
	return polar(complex(lhs) - complex(rhs));
}

polar math::operator*(const polar lhs, const polar rhs)
{
	return polar();
}

polar math::operator/(const polar lhs, const polar rhs)
{
	return polar();
}

polar math::operator+(const polar lhs, const double rhs)
{
	return polar();
}

polar math::operator-(const polar lhs, const double rhs)
{
	return polar();
}

polar math::operator*(const polar lhs, const double rhs)
{
	return polar();
}

polar math::operator/(const polar lhs, const double rhs)
{
	return polar();
}

polar math::operator+(const double lhs, const polar rhs)
{
	return polar();
}

polar math::operator-(const double lhs, const polar rhs)
{
	return polar();
}

polar math::operator*(const double lhs, const polar rhs)
{
	return polar();
}

polar math::operator/(const double lhs, const polar rhs)
{
	return polar();
}

polar math::operator+(const polar lhs, const complex rhs)
{
	return polar();
}

polar math::operator-(const polar lhs, const complex rhs)
{
	return polar();
}

polar math::operator*(const polar lhs, const complex rhs)
{
	return polar();
}

polar math::operator/(const polar lhs, const complex rhs)
{
	return polar();
}

double math::real(const polar p)
{
	return p.abs * cos(p.phi);
}

double math::real(const complex c)
{
	return c.x;
}

double math::imaginary(const polar p)
{
	return p.abs * sin(p.phi);
}

double math::imaginary(const complex c)
{
	return c.imaginary;
}

polar math::conj(const polar p)
{
	return polar();
}

complex math::conj(const complex c)
{
	return complex(c.x, -c.i);
}

polar math::conjugate(const polar p)
{
	return conj(p);
}

complex math::conjugate(const complex c)
{
	return conj(c);
}

double math::projection(const polar p)
{
	return real(p);
}

double math::projection(const complex c)
{
	return c.x;
}

double math::projectionOn(const polar p)
{
	return 0.0;
}

double math::projectionOn(const complex c)
{
	return 0.0;
}

double math::norm(const polar p)
{
	return p.abs * p.abs;
}

double math::norm(const complex c)
{
	return (c.x * c.x) + (c.y * c.y);
}

double math::abs(const polar p)
{
	return p.abs;
}

double math::abs(const complex c)
{
	return sqrt(norm(c));
}

double math::absolute(const polar p)
{
	return p.abs;
}

double math::absolute(const complex c)
{
	return abs(c);
}

angle math::arg(const polar p)
{
	return p.arg;
}

angle math::arg(const complex c)
{
	return angle(atan2(c.y, c.x));
}

angle math::argument(const polar p)
{
	return p.arg;
}

angle math::argument(const complex c)
{
	return arg(c);
}

angle math::phi(const polar p)
{
	return p.arg;
}

angle math::phi(const complex c)
{
	return arg(c);
}

angle math::phase(const polar p)
{
	return p.arg;
}

angle math::phase(const complex c)
{
	return arg(c);
}
