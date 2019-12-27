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
		virtual operator bool() const;
		virtual operator int() const;
		virtual operator float() const;
		virtual operator double() const;
		virtual bool		operator!	() const;
		virtual Numeric		operator~	() const;
		virtual Numeric		operator+	() const;
		virtual Numeric		operator-	() const;
		virtual Numeric		operator++	();
		virtual Numeric		operator++	(int);
		virtual Numeric		operator--	();
		virtual Numeric		operator--	(int);
		virtual Numeric		operator%	(Numeric&) const;
		virtual Numeric&	operator%=	(Numeric&);
		virtual Numeric		operator*	(Numeric&) const;
		virtual Numeric&	operator*=	(Numeric&);
		virtual Numeric		operator+	(Numeric&) const;
		virtual Numeric&	operator+=	(Numeric&);
		virtual Numeric		operator-	(Numeric&) const;
		virtual Numeric&	operator-=	(Numeric&);
		virtual Numeric		operator/	(Numeric&) const;
		virtual Numeric&	operator/=	(Numeric&);
		virtual bool		operator!=	(Numeric&) const;
		virtual bool		operator&&	(Numeric&) const;
		virtual bool		operator||	(Numeric&) const;
		virtual bool		operator<	(Numeric&) const;
		virtual bool		operator<=	(Numeric&) const;
		virtual bool		operator>	(Numeric&) const;
		virtual bool		operator>=	(Numeric&) const;
		virtual bool		operator==	(Numeric&) const;

	} numeric;
}