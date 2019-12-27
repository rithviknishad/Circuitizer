#include "Complex.h"

namespace math
{
	void Complex::Set(double real, double imaginary) { m_real = real; m_imaginary = imaginary; }

	void Complex::Set(Complex& c) { m_real = c.m_real; m_imaginary = c.m_imaginary; }

	std::pair<double, double> Complex::Get() const { return std::pair<double, double>(m_real, m_imaginary); }
	std::string Complex::ToString() const
	{
		std::stringstream ss;
		ss << m_real << " + " << m_imaginary << "i";
		return ss.str();
	}

	double real(const Complex& c)			{ return c.m_real; }
	double imaginary(const Complex& c)	{ return c.m_imaginary; }
	angle phase(const Complex& c)			{ return angle(atan2(c.m_imaginary, c.m_real)); }
	double magnitude(const Complex& c)	{ return sqrt((c.m_imaginary * c.m_imaginary) + (c.m_real * c.m_real)); }
	Complex conjugate(const Complex& c)	{ return Complex(c.m_real, -c.m_imaginary); }
}