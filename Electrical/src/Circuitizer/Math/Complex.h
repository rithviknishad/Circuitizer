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
		void Set(double real, double imaginary);
		void Set(Complex& c);
		std::pair<double, double> Get() const;

		virtual std::string ToString() const;

	public:
		friend double real(Complex& c);
		friend double imaginary(Complex& c);
		friend angle phase(Complex& c);
		friend double magnitude(Complex& c);
		friend Complex conjugate(Complex& c);

	protected:
		double m_real, m_imaginary;

	} complex;

	double real(Complex& c);
	double imaginary(Complex& c);
	angle phase(Complex& c);
	double magnitude(Complex& c);
	Complex conjugate(Complex& c);

	inline std::ostream& operator<< (std::ostream& os, const Complex& c) { return os << c.ToString(); }
}