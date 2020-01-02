#pragma once

#include "crpch.h"

namespace Circuitizer
{
	class Position
	{
	public:
		Position(const int x = 0, const int y = 0, const int z = 0) : m_PosX(x), m_PosY(y), m_PosZ(z) {}

		inline void SetPosition(const int x, const int y, const int z)
		{
			m_PosX = x;
			m_PosY = y;
			m_PosZ = z;
		}

		inline void SetPosX(const int x) { m_PosX = x; }
		inline void SetPosY(const int y) { m_PosY = y; }
		inline void SetPosZ(const int z) { m_PosZ = z; }

		inline std::tuple<int, int, int> GetPosition() { return { m_PosX, m_PosY, m_PosZ }; }

		inline int GetPosX() { return m_PosX; }
		inline int GetPosY() { return m_PosY; }
		inline int GetPosZ() { return m_PosZ; }

	protected:
		int m_PosX, m_PosY, m_PosZ;

	};

	static const Position Origin = Position(0, 0, 0);
}