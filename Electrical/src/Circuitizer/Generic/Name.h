#pragma once
#include "crpch.h"

namespace Circuitizer
{
	class Name
	{
	public:
		/* Constructs a virtual Name property class with the specified name*/
		Name(std::string name) : m_Name(name) {}

		/* Returns the name of the entity. */
		inline virtual std::string GetName() { return m_Name; }
		inline operator std::string() { return m_Name; }

		/* Sets the name of the entity. */
		inline virtual void SetName(std::string name) { m_Name = name; }
		inline Name& operator=(std::string name) { m_Name = name; return *this; }

	protected:
		std::string m_Name;
	};
}