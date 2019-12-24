#pragma once

#include "crpch.h"

class Name
{
public:
	Name(std::string name) : m_Name(name)
	{
	}

	std::string GetName() { return m_Name; }
	virtual void SetName(std::string name) { m_Name = name; }

protected:
	std::string m_Name;
};