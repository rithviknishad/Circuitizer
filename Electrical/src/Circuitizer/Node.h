#pragma once

#include "crpch.h"
#include "Core.h"

class Terminal;

namespace Electrical
{
	/*
	A node is any point on a circuit where the terminals of two or more circuit elements meet.
	In circuit diagrams, connections are ideal wires with zero resistance, so a node may 
	consist of the entire section of wire between elements, not just a single point.
	*/
	class CIRCUITIZER_API Node
	{
	public:
		
		/*
		Create a Node.
		Specify a name for the node.
		*/
		Node(std::string name = "") : m_Name(name) {}
		
		~Node() {}

		/*
		Returns the name of the Node as a string.
		*/
		inline std::string GetName() { return m_Name; }

		/*
		Sets the name of the Node.
		*/
		inline void SetName(std::string name) { m_Name = name; }

		/*
		Attaches a terminal to the node and returns the Node pointer.
		Note: Pass a Terminal* (pointer to the terminal).
		*/
		inline Node* ConnectTerminal(Terminal* terminal) { m_Terminals.push_back(terminal); return this; }

		/*
		Attaches terminals to the node and returns the Node pointer.
		Note: Pass a vector<Terminal*> (list of pointers to the terminals).
		*/
		inline Node* ConnectTerminals(std::vector<Terminal*> terminals)
		{
			for (Terminal* terminal : terminals)
				m_Terminals.push_back(terminal);
			return this;
		}

		/*
		Detaches the terminal from the node.
		Note: Pass a Terminal* (pointer to the terminal).
		*/
		inline void DisconnectTerminal(Terminal* terminal)
		{ 
			m_Terminals.erase(std::remove(m_Terminals.begin(), m_Terminals.end(), terminal), m_Terminals.end());
		}

		/*
		Disconnects all terminals from the node.
		*/
		inline void DisconnectAllTerminals() { m_Terminals.clear(); }

		/*
		Merges two node and creates a new node.
		*/
		inline Node* MergeNode(Node* node)
		{
			ConnectTerminals(node->GetTerminals());
			node->DisconnectAllTerminals();
			return this;
		}


		/*
		Returns a std::vector of Terminal pointers associated with the node.
		*/
		inline std::vector<Terminal*> GetTerminals() { return m_Terminals; }

	private:

		std::string m_Name;
		std::vector<Terminal*> m_Terminals;
	};
}