#pragma once

#include "emath.h"

typedef double angle;

namespace math
{
#pragma region angle

	double absolute_angle(double val, double lim)
	{
		if (val < 0.0)
			val += (((int)(-val / lim)) + 1.00) * lim;
		else if (val >= lim)
			val -= ((int)(val / lim)) * lim;

		return val;
	}

	angle abs_rad(angle theta) { return absolute_angle((double)theta, pi2); }
	angle abs_deg(angle theta) { return absolute_angle((double)theta, 360.0); }
	angle abs_grad(angle theta) { return absolute_angle((double)theta, 100.0); }

	angle radian(double degree) { return angle(degree * pi / 180.0); }
	double degree(angle radian) { return radian * 180.0 / pi; }

#pragma endregion
}