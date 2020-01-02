#pragma once

#include "crpch.h"
#include "Terminal.h"

namespace Circuitizer
{
	typedef class TerminalContainer
	{
	public:
		TerminalContainer();
		~TerminalContainer();

		/* Binds specified amount of terminals to the component. */
		void AddTerminals(int count, std::string prefix_str = "");

		/* Binds specified terminal to the component. */
		void AddTerminal(Terminal* terminal);

		/* Unbinds the specified terminal from component. */
		void RemoveTerminal(Terminal* terminal, bool deleteFlag = false);

		/* Returns the list of terminal pointers as a vector */
		std::vector<Terminal*> GetTerminals();

	protected:
		std::vector<Terminal*> m_Terminals;
	} Terminals;
}