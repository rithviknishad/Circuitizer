#pragma once

namespace math
{

// mathematical constants
#define pi 3.14159265358979
#define pi2 6.2831853071795
#define piby2 1.5707963267949
#define pi3by2 4.71238898038468

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
		Angle		operator+	();
		Angle		operator-	();
		Angle		operator++	();
		Angle		operator++	(int);
		Angle		operator--	();
		Angle		operator--	(int);
		Angle		operator%	(Angle&);
		Angle&		operator%=	(Angle&);
		Angle		operator+	(Angle&);
		Angle&		operator+=	(Angle&);
		Angle		operator-	(Angle&);
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
		Angle		operator*	(const double);
		Angle&		operator*=	(const double);
		Angle		operator+	(const double);
		Angle&		operator+=	(const double);
		Angle		operator-	(const double);
		Angle&		operator-=	(const double);
		Angle		operator/	(const double);
		Angle&		operator/=	(const double);
		bool		operator!=	(const double);
		bool		operator<	(const double);
		bool		operator<=	(const double);
		bool		operator>	(const double);
		bool		operator>=	(const double);
		bool		operator==	(const double);

	private:
		double m_value;
	} angle;

}