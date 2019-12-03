#include "../math/complex.h"
#include "power.h"

using namespace e;

e::power::power() : A()
{
}

e::power::power(complex c) : A(c)
{
}

e::power::power(const double p, const double q) : A(p, q)
{
}

e::power::power(polar p) : A(p)
{
}

e::power::power(const double _abs, const angle _phi) : A(_abs, _phi)
{
}

power& e::power::fromComplex(const complex c)
{
	S = complex(c);
	return *this;
}

power& e::power::fromComplex(const double p, const double q)
{
	S = complex(p, q);
	return *this;
}

power& e::power::fromPolar(const polar p)
{
	S = complex(p);
	return *this;
}

power& e::power::fromPolar(const double _abs, const double _phi_d)
{
	S = complex().fromPolar(_abs, _phi_d);
	return *this;
}

power& e::power::fromPolar(const double _abs, const angle _phi)
{
	S = complex().fromPolar(_abs, _phi);
	return *this;
}
