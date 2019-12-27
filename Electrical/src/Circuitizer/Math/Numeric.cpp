#include "Numeric.h"

namespace math
{
	Numeric& Numeric::operator=(double value) { m_real = value; return *this; }
	Numeric::operator bool() const		{ return m_real == 0.0 && m_imaginary == 0.0; }
	Numeric::operator int() const		{ return (int)magnitude(*this); }
	Numeric::operator float() const		{ return (float)magnitude(*this); }
	Numeric::operator double() const	{ return (double)magnitude(*this); }

	bool Numeric::operator!() const { return !bool(*this); }

	Numeric Numeric::operator~() const { return Numeric(conjugate(*this)); }
	Numeric Numeric::operator+() const { return Numeric(*this); }
	Numeric Numeric::operator-() const { return Numeric(-m_real, -m_imaginary); }

	Numeric Numeric::operator++()		{ return Numeric(++m_real, ++m_imaginary); }
	Numeric Numeric::operator++(int)	{ return Numeric(m_real++, m_imaginary++); }
	Numeric Numeric::operator--()		{ return Numeric(--m_real, --m_imaginary); }
	Numeric Numeric::operator--(int)	{ return Numeric(m_real--, m_imaginary--); }
	// TODO
	Numeric Numeric::operator%(Numeric& n) const
	{
		//return Numeric();
	}
	// TODO
	Numeric& Numeric::operator%=(Numeric& n)
	{
		// TODO: insert return statement here
	}
	Numeric Numeric::operator*(Numeric& n) const	{ return Numeric((m_real * real(n)) - (m_imaginary * imaginary(n)), (m_real * imaginary(n)) + (m_imaginary * real(n))); }
	Numeric& Numeric::operator*=(Numeric& n)		{ Set(*this * n); return *this; }
	Numeric Numeric::operator+(Numeric& n) const	{ return Numeric(m_real + n.m_real, m_imaginary + n.m_imaginary); }
	Numeric& Numeric::operator+=(Numeric& n)		{ m_real += n.m_real; m_imaginary += n.m_imaginary; return *this; }
	Numeric Numeric::operator-(Numeric& n) const	{ return Numeric(m_real - n.m_real, m_imaginary - n.m_imaginary); }
	Numeric& Numeric::operator-=(Numeric& n)		{ m_real -= n.m_real; m_imaginary -= n.m_imaginary; return *this; }

	Numeric Numeric::operator/(Numeric& n) const
	{
		const double d = magnitude(n);
		return Numeric(((m_real * real(n)) + (m_imaginary * imaginary(n))) / d, ((m_imaginary * real(n)) - (m_real * imaginary(n))) / d);
	}
	Numeric& Numeric::operator/=(Numeric& n) { Set(*this / n); return *this; }

	bool Numeric::operator!=(Numeric& n) const { return !((*this) == n); }
	bool Numeric::operator&&(Numeric& n) const { return bool(*this) && bool(n); }
	bool Numeric::operator||(Numeric& n) const { return bool(*this) || bool(n); }
	
	bool Numeric::operator<(Numeric& n) const	{ return magnitude(*this) < magnitude(n); }
	bool Numeric::operator<=(Numeric& n) const	{ return magnitude(*this) <= magnitude(n); }
	bool Numeric::operator>(Numeric& n) const	{ return magnitude(*this) > magnitude(n); }
	bool Numeric::operator>=(Numeric& n) const	{ return magnitude(*this) >= magnitude(n); }

	bool Numeric::operator==(Numeric& n)  const { return m_real == n.m_real && m_imaginary == n.m_imaginary; }
}