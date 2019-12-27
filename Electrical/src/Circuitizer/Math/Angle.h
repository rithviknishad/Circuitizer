#pragma once

#include "crpch.h"

namespace math
{
	// mathematical constants
	const double pi = 3.14159265358979;
	const double pi2 = 6.2831853071795;
	const double piby2 = 1.5707963267949;
	const double pi3by2 = 4.71238898038468;

	// mathematical symbols
	const char PHI = char(237);
	const char PI  = char(227);

	double __absangle(double& val);

	typedef class Angle
	{
	public:
		Angle(double value = 0.0) : m_value(value) {}

		operator bool();
		operator double();
		operator float();
		operator int();

		void operator=(double value);

		bool		operator!	();
		Angle		operator+	() const;
		Angle		operator-	() const;
		Angle		operator++	();
		Angle		operator++	(int);
		Angle		operator--	();
		Angle		operator--	(int);
		Angle		operator%	(Angle&);
		Angle&		operator%=	(Angle&);
		Angle		operator+	(Angle&) const;
		Angle&		operator+=	(Angle&);
		Angle		operator-	(Angle&) const;
		Angle&		operator-=	(Angle&);
		bool		operator!=	(Angle&);
		bool		operator&&	(Angle&);
		bool		operator||	(Angle&);
		bool		operator<	(Angle&);
		bool		operator<=	(Angle&);
		bool		operator>	(Angle&);
		bool		operator>=	(Angle&);
		bool		operator==	(Angle&);
		Angle		operator%	(const double);
		Angle&		operator%=	(const double);
		Angle		operator*	(const double) const;
		Angle&		operator*=	(const double);
		Angle		operator+	(const double) const;
		Angle&		operator+=	(const double);
		Angle		operator-	(const double) const;
		Angle&		operator-=	(const double);
		Angle		operator/	(const double) const;
		Angle&		operator/=	(const double);
		bool		operator!=	(const double);
		bool		operator<	(const double);
		bool		operator<=	(const double);
		bool		operator>	(const double);
		bool		operator>=	(const double);
		bool		operator==	(const double);

		std::string ToString() const;

	private:
		double m_value;
	} angle;

	inline std::ostream& operator<< (std::ostream& os, const Angle& a) { return os << a.ToString(); }
}