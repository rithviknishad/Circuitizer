#pragma once

#include "crpch.h"
#include "Core.h"
#include "Node.h"

namespace Electrical
{
	/*
	A terminal is the point at which a conductor from a component, device or network comes to an end. 
	Terminal may also refer to an electrical connector at this endpoint, acting as the reusable 
	interface to a conductor and creating a point where external circuits can be connected.
	*/
	class CIRCUITIZER_API Terminal
	{
	public:
		Terminal(std::string name = "") : m_Name(name) {}
		~Terminal() {}

		/*
		Returns the name of the terminal as a string.
		*/
		inline std::string GetName() { return m_Name; }

		/*
		Sets the name of the Terminal.
		*/
		inline void SetName(std::string name) { m_Name = name; }

		/*
		Connects two terminals and generates a node.
		If any of the terminal is already connected to a node, a node merge is performed
		*/
		inline Node* ConnectToTerminal(Terminal* terminal)
		{
			if (m_Node != nullptr)
			{
				if (terminal->ConnectedNode() != nullptr)
				{
					for (Terminal* t : terminal->ConnectedNode()->GetTerminals())
						t->ConnectToNode(m_Node);
				}
				else
					return terminal->ConnectToNode(m_Node);
			}
			else
			{
				if (terminal->ConnectedNode() == nullptr)
					return ConnectToNode(terminal->ConnectToNode(new Node));
				else
					return terminal->ConnectToTerminal(this);
			}
			return m_Node;
		}

		/*
		Returns the Node pointer to which the terminal is connected to.
		Note: A terminal can be connected only to one node.
		*/
		inline Node* ConnectedNode() { return m_Node; }

		/*
		Connects the terminal to the specified node, after disconnecting from previously connected node (if any), and returns the new node.
		Note: A terminal can be connected only to one node.
		*/
		inline Node* ConnectToNode(Node* node)
		{ 
			if (m_Node != nullptr)
				m_Node->DisconnectTerminal(this);
			
			return (m_Node = node->ConnectTerminal(this));
		}

		/*
		Disconnects from connected node (if any)
		*/
		inline Node* DisconnectFromNode()
		{
			if (m_Node != nullptr)
				m_Node->DisconnectTerminal(this);
			m_Node = nullptr;
		}
	
		double Voltage = 0.0;

	private:
		std::string m_Name;
		Node* m_Node = nullptr;
	};
}