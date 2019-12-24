#pragma once

#include "crpch.h"
#include "Angle.h"

namespace math
{
	typedef class Complex
	{
	public:
		Complex(double real = 0.0, double imaginary = 0.0) : m_real(real), m_imaginary(imaginary) {}
		Complex(Complex& c) : m_real(c.m_real), m_imaginary(c.m_imaginary) {}

	public:
		inline void Set(double real, double imaginary);
		std::pair<double, double> Get() const;

		virtual std::string ToString() const;

	public:
		friend double real(Complex& c);
		friend double imaginary(Complex& c);
		friend Complex conjugate(Complex& c);

	protected:
		double m_real, m_imaginary;

	} complex;

	Complex add(Complex a, Complex b);
	Complex subtract(Complex a, Complex b);
	Complex multiply(Complex a, Complex b);
	Complex divide(Complex a, Complex b);

	double real(Complex& c);
	double imaginary(Complex& c);
	angle phase(Complex& c);
	double magnitude(Complex& c);
	Complex conjugate(Complex& c);

	inline std::ostream& operator<< (std::ostream& os, const Complex& c) { return os << c.ToString(); }
}