#pragma once

#include "crpch.h"
#include "Core.h"

#include "Terminal.h"

namespace Electrical
{
	class CIRCUITIZER_API Component
	{
	public:
		Component(std::string name = "") : m_Name(name) {}
		virtual ~Component();

		std::string GetName() { return m_Name; }

		inline void AddTerminal(std::string name)
		{ 
			Terminals.push_back(new Terminal(name));

			Terminals[0]->ConnectedNode();

		}
		
		inline std::vector<Terminal*> GetTerminals() { return Terminals; }

	private:
		std::string m_Name;
		std::vector<Terminal*> Terminals;
	};
}