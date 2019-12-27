#include "Angle.h"

namespace math
{
    double __absangle(double& val)
    {
        if (val < 0.0)
            val += (((int)(-val / pi2)) + 1.00) * pi2;
        else if (val >= pi2)
            val -= ((int)(val / pi2)) * pi2;
        return val;
    }

	Angle::operator bool()		{ return __absangle(m_value) != 0.0; }
	Angle::operator double()	{ return __absangle(m_value); }
	Angle::operator float()		{ return float(__absangle(m_value)); }
	Angle::operator int()		{ return int(__absangle(m_value)); }
	
	void Angle::operator=(double value) { m_value = __absangle(value); }
	
	bool Angle::operator!() { return !bool(*this); }
	
	Angle Angle::operator+() const { return Angle(m_value); }
	Angle Angle::operator-() const { return Angle(m_value + pi); }

	Angle Angle::operator++() { return Angle(++m_value); }
	Angle Angle::operator++(int) { return Angle(m_value++); }
	Angle Angle::operator--() { return Angle(--m_value); }
	Angle Angle::operator--(int) { return Angle(m_value--); }

	Angle Angle::operator%	(Angle& a) { return Angle(double(*this) - (int(double(*this) / double(a)) * double(a))); }
	Angle& Angle::operator%=(Angle& a) { m_value = double(*this) - (int(double(*this) / double(a)) * double(a)); return *this; }
	Angle Angle::operator+	(Angle& a) const { return Angle(m_value + a.m_value); }
	Angle& Angle::operator+=(Angle& a) { m_value += a.m_value; return *this; }
	Angle Angle::operator-	(Angle& a) const { return Angle(m_value - a.m_value); }
	Angle& Angle::operator-=(Angle& a) { m_value -= a.m_value; return *this; }

	bool Angle::operator!=(Angle& a) { return float(*this) != float(a); }
	bool Angle::operator&&(Angle& a) { return bool(*this) && bool(a); }
	bool Angle::operator||(Angle& a) { return bool(*this) || bool(a); }
	bool Angle::operator< (Angle& a) { return float(*this) < float(a); }
	bool Angle::operator<=(Angle& a) { return float(*this) <= float(a); }
	bool Angle::operator> (Angle& a) { return float(*this) > float(a); }
	bool Angle::operator>=(Angle& a) { return float(*this) >= float(a); }
	bool Angle::operator==(Angle& a) { return float(*this) == float(a); }

	Angle Angle::operator%	(const double a) { return Angle(double(*this) - (int(double(*this) / __absangle(double(a))) * __absangle(double(a)))); }
	Angle& Angle::operator%=(const double a) { m_value = double(*this) - (int(double(*this) / __absangle(double(a))) * __absangle(double(a))); return *this; }
	Angle Angle::operator*	(const double a) const { return Angle(m_value * a); }
	Angle& Angle::operator*=(const double a) { m_value *= a; return *this; }
	Angle Angle::operator+	(const double a) const { return Angle(m_value + a); }
	Angle& Angle::operator+=(const double a) { m_value += a; return *this; }
	Angle Angle::operator-	(const double a) const { return Angle(m_value - a); }
	Angle& Angle::operator-=(const double a) { m_value -= a; return *this; }
	Angle Angle::operator/	(const double a) const
	{
		if (a != 0.0)
			return Angle(m_value / a);
		else
			throw "Div by 0";
		return Angle();
	}
	Angle& Angle::operator/=(const double a)
	{
		if (a != 0.0)
			m_value /= a;
		else
			throw "Div by 0";
		return *this;
	}

	bool Angle::operator!=	(const double a) { return float(*this) != float(a); }
	bool Angle::operator<	(const double a) { return float(*this) < float(a); }
	bool Angle::operator<=	(const double a) { return float(*this) <= float(a); }
	bool Angle::operator>	(const double a) { return float(*this) > float(a); }
	bool Angle::operator>=	(const double a) { return float(*this) >= float(a); }
	bool Angle::operator==	(const double a) { return float(*this) == float(a); }
	std::string Angle::ToString() const
	{ 
		std::stringstream ss;
		ss << PHI << " = " << float(m_value / pi) << PI << " rad";
		return ss.str();
	}
}