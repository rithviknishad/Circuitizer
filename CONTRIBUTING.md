# Contributing Guidelines

## Naming conventions

### Casing

lowercase for numerical constants
uppercase for literal symbols

**Example:**
```cpp
#define pi	3.14159265358979	// double Pi
#define PI	char(227)		// 'π' symbol
#define PHI	char(237)		// 'φ' symbol
```

### Prefixes and suffixes

* When symbol prefixed with **'_d'** it refers to a **double type**. Otherwise it refers to an object.

**Example:**
```cpp
angle phi = angle();
double phi_d = phi.radian;
```



## Standards in units:
__All measurement units by default is in SI units.__
Except the ones which are in *bold* below.

### Unit reference:
- Angle			Radians
- Distance		Meters