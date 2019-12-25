#include "Numeric.h"

namespace math
{
	Numeric::operator bool() { return m_real == 0.0 && m_imaginary == 0.0; }

	bool Numeric::operator!() { return !bool(*this); }

	Numeric Numeric::operator~() { return Numeric(conjugate(*this)); }
	
	Numeric Numeric::operator+() { return Numeric(*this); }
	Numeric Numeric::operator-() { return Numeric(-m_real, -m_imaginary); }

	Numeric Numeric::operator++()		{ return Numeric(++m_real, ++m_imaginary); }
	Numeric Numeric::operator++(int)	{ return Numeric(m_real++, m_imaginary++); }
	Numeric Numeric::operator--()		{ return Numeric(--m_real, --m_imaginary); }
	Numeric Numeric::operator--(int)	{ return Numeric(m_real--, m_imaginary--); }
	// TODO
	Numeric Numeric::operator%(Numeric& n)
	{
		return Numeric();
	}
	// TODO
	Numeric& Numeric::operator%=(Numeric& n)
	{
		// TODO: insert return statement here
	}
	Numeric Numeric::operator*(Numeric& n)
	{
		return Numeric();
	}
	Numeric& Numeric::operator*=(Numeric& n)
	{
		// TODO: insert return statement here
	}
	Numeric Numeric::operator+(Numeric& n)
	{
		return Numeric();
	}
	Numeric& Numeric::operator+=(Numeric& n)
	{
		// TODO: insert return statement here
	}
	Numeric Numeric::operator-(Numeric& n)
	{
		return Numeric();
	}
	Numeric& Numeric::operator-=(Numeric& n)
	{
		// TODO: insert return statement here
	}
	Numeric Numeric::operator/(Numeric& n)
	{
		return Numeric();
	}
	Numeric& Numeric::operator/=(Numeric& n)
	{
		// TODO: insert return statement here
	}

	bool Numeric::operator!=(Numeric& n) { return !((*this) == n); }
	bool Numeric::operator&&(Numeric& n) { return bool(*this) && bool(n); }
	bool Numeric::operator||(Numeric& n) { return bool(*this) || bool(n); }
	
	bool Numeric::operator<(Numeric& n) { return magnitude(*this) < magnitude(n); }
	bool Numeric::operator<=(Numeric& n) { return magnitude(*this) <= magnitude(n); }
	bool Numeric::operator>(Numeric& n) { return magnitude(*this) > magnitude(n); }
	bool Numeric::operator>=(Numeric& n) { return magnitude(*this) >= magnitude(n); }

	bool Numeric::operator==(Numeric& n) { return m_real == n.m_real && m_imaginary == n.m_imaginary; }
}