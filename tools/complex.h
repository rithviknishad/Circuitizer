
namespace math
{
	typedef struct angle
	{
		double value;

		angle();
		angle(double val);

		angle& operator+=(const angle& rhs);
		angle& operator-=(const angle& rhs);
		angle& operator*=(const double factor);
		angle& operator/=(const double factor);

		angle& makeabsolute();
		angle& getabsolute();
	};

	angle& operator+(const angle& lhs, const angle& rhs);
	angle& operator-(const angle& lhs, const angle& rhs);
	angle& operator*(const angle& lhs, const double factor);
	angle& operator/(const angle& lhs, const double factor);
	angle& operator*(const double factor, const angle& lhs);
	angle& operator/(const double factor, const angle& lhs);



	typedef struct complex
	{
		double real, imaginary;
	};

	typedef struct polar
	{
		double magnitude;
		angle direction;
	};
}