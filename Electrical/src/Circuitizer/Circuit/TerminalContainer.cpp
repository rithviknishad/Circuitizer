#include "TerminalContainer.h"

namespace Circuitizer
{
	TerminalContainer::TerminalContainer() {}

	TerminalContainer::~TerminalContainer()
	{
		for (Terminal* terminal : m_Terminals)
			RemoveTerminal(terminal, true);
	}

	void TerminalContainer::AddTerminals(int count, std::string prefix_str)
	{
		for (int i = 0; i < count; ++i)
			m_Terminals.push_back(new Terminal(prefix_str + "_PIN" + std::to_string(m_Terminals.size())));
	}

	void TerminalContainer::AddTerminal(Terminal* terminal)
	{
		m_Terminals.push_back(terminal); 
	}

	void TerminalContainer::RemoveTerminal(Terminal* terminal, bool deleteFlag = true)
	{
		m_Terminals.erase(std::remove(m_Terminals.begin(), m_Terminals.end(), terminal), m_Terminals.end());

		if (deleteFlag)
			delete terminal;
	}

	std::vector<Terminal*> TerminalContainer::GetTerminals()
	{ 
		return m_Terminals;
	}
}