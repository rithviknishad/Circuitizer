#pragma once

#include "crpch.h"
#include "Circuitizer/Core.h"

#include "Circuitizer/Terminal.h"

namespace Electrical
{
	class CIRCUITIZER_API Component
	{
	public:
		Component(std::string name = "") : m_Name(name) {}
		virtual ~Component() = 0;

		/* Returns the name of the Component as a string */
		std::string GetName() { return m_Name; }

		/* Sets the name of the Component. */
		virtual void SetName(std::string name) { m_Name = name; }

		/*
		Associates specified amount of terminals to the component.
		Naming convention: "<ComponentName>_PIN<TerminalIndex>"
		*/
		inline void AddTerminals(int count = 1)
		{
			for (int i = 0; i < count; ++i)
				m_Terminals.push_back(new Terminal(m_Name + "_PIN" + std::to_string(m_Terminals.size())));
		}

		/* Assosciates the specified terminal to the component. */
		inline void AddTerminal(Terminal* terminal) { m_Terminals.push_back(terminal); }

		/* Disassociates the specified terminal from component. */
		inline void RemoveTerminal(Terminal* terminal, bool)
		{
			m_Terminals.erase(std::remove(m_Terminals.begin(), m_Terminals.end(), terminal), m_Terminals.end());
		}



		inline std::vector<Terminal*> GetTerminals() { return m_Terminals; }

	protected:
		std::vector<Terminal*> m_Terminals;

	private:
		std::string m_Name;
	};
}