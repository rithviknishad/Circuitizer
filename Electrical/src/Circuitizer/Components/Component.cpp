#include "Component.h"

namespace Electrical
{
	Component::Component(std::string name, int pinCount, Position position)
		: Name(name), Position(position)
	{
		AddTerminals(pinCount);
	}

	void Component::AddTerminals(int count)
	{
		for (int i = 0; i < count; ++i)
			m_Terminals.push_back(new Terminal(m_Name + "_PIN" + std::to_string(m_Terminals.size())));
	}

	void Component::AddTerminal(Terminal* terminal) { m_Terminals.push_back(terminal); }

	void Component::RemoveTerminal(Terminal* terminal, bool deleteFlag)
	{
		m_Terminals.erase(std::remove(m_Terminals.begin(), m_Terminals.end(), terminal), m_Terminals.end());
		
		if (deleteFlag)
			delete terminal;
	}

	Terminals Component::GetTerminals() { return m_Terminals; }
	Component::operator Terminals() { return m_Terminals; }
}