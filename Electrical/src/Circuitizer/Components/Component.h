#pragma once

//#include "crpch.h"
#include "Circuitizer/Generic/Generics.h"
#include "Circuitizer/Terminal.h"

namespace Electrical
{
	class Component : public Name, public Position
	{
	public:
		Component(std::string name = "") : Name(name), Position(0, 0) {}
		virtual ~Component() = 0;

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

		/* Updates the component for time change */
		virtual void OnUpdate(double time) = 0;

		inline std::vector<Terminal*> GetTerminals() { return m_Terminals; }

	protected:
		std::vector<Terminal*> m_Terminals;
	};
}