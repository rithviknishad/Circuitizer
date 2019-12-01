#ifndef POWER_H
#define POWER_H

#include "../math/complex.h"

namespace e
{
	typedef struct power : struct complex
	{
		using base_complex = complex;

		union
		{
			complex
		};

	};
}

#endif // !POWER_H