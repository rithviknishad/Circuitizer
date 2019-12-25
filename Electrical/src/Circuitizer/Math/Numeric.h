#pragma once

#include "Complex.h"

namespace math
{

	typedef class Numeric : public Complex
	{
	public:

		Numeric(double real = 0.0, double imaginary = 0.0) : Complex(real, imaginary) {}
		Numeric(std::pair<double, double> value) : Complex(value.first, value.second) {}
		Numeric(Complex& c) : Complex(c) {}

		// ==========  Operator Overloads  ==========

		virtual Numeric& operator=(double);
		virtual operator bool();
		virtual operator int();
		virtual operator float();
		virtual operator double();
		virtual bool		operator!	();
		virtual Numeric		operator~	();
		virtual Numeric		operator+	();
		virtual Numeric		operator-	();
		virtual Numeric		operator++	();
		virtual Numeric		operator++	(int);
		virtual Numeric		operator--	();
		virtual Numeric		operator--	(int);
		virtual Numeric		operator%	(Numeric&);
		virtual Numeric&	operator%=	(Numeric&);
		virtual Numeric		operator*	(Numeric&);
		virtual Numeric&	operator*=	(Numeric&);
		virtual Numeric		operator+	(Numeric&);
		virtual Numeric&	operator+=	(Numeric&);
		virtual Numeric		operator-	(Numeric&);
		virtual Numeric&	operator-=	(Numeric&);
		virtual Numeric		operator/	(Numeric&);
		virtual Numeric&	operator/=	(Numeric&);
		virtual bool		operator!=	(Numeric&);
		virtual bool		operator&&	(Numeric&);
		virtual bool		operator||	(Numeric&);
		virtual bool		operator<	(Numeric&);
		virtual bool		operator<=	(Numeric&);
		virtual bool		operator>	(Numeric&);
		virtual bool		operator>=	(Numeric&);
		virtual bool		operator==	(Numeric&);

	} numeric;
}