#include "Complex.h"

namespace math
{
	void Complex::Set(double real, double imaginary)
	{
		m_real = real;
		m_imaginary = imaginary;
	}

	std::pair<double, double> Complex::Get() const { return std::pair<double, double>(m_real, m_imaginary); }
	std::string Complex::ToString() const { return std::string(); }

	double real(Complex& c) { return c.m_real; }
	double imaginary(Complex& c) { return c.m_imaginary; }
	Complex conjugate(Complex& c) { return Complex(c.m_real, -c.m_imaginary); }
}