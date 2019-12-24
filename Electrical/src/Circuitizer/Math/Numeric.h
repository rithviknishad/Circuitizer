#pragma once

#include "Complex.h"

namespace math
{

	typedef class Numeric : public Complex
	{
	public:

		Numeric(double real = 0.0, double imaginary = 0.0) : Complex(real, imaginary) {}
		Numeric(Complex& c) : Complex(c) {}

		// ==========  Operator Overloads  ==========

		virtual operator bool();
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

	void e()
	{
		numeric a;
		double b = real(a);
	}
}