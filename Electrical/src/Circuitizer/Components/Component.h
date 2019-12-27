#pragma once

#include "crpch.h"
#include "Circuitizer/Generic/Generics.h"
#include "Circuitizer/Circuit/Terminal.h"

namespace Electrical
{
	typedef std::vector<Terminal*> Terminals;

	class Component : public Name, public Position
	{
	public:
		Component(std::string name, int pinCount, Position position);
		virtual ~Component() = 0;

		/* Associates specified amount of terminals to the component. */
		void AddTerminals(int count = 1);

		/* Binds the specified terminal to the component. */
		void AddTerminal(Terminal* terminal);

		/* Unbinds the specified terminal from component. */
		void RemoveTerminal(Terminal* terminal, bool deleteFlag = false);

		/* Returns the terminals of the component. */
		Terminals GetTerminals();
		operator Terminals();

	protected:
		Terminals m_Terminals;
	};
}