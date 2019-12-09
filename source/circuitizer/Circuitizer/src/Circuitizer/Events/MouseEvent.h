#pragma once

#include "Event.h"

#include <sstream>

namespace Circuitizer
{
	class CIRCUITIZER_API MouseMovedEvent : public Event
	{
	public:
		
		MouseMovedEvent(float x, float y) : m_MouseX(x), m_MouseY(y)
		{
		}

		inline float GetX() const { return m_MouseX; }
		inline float GetY() const { return m_MouseY; }

		std::string ToString() const override
		{
			std::stringstream ss;
			ss << "MouseMovedEvent: " << m_MouseX << ", " << m_MouseY;
			return ss.str;
		}

		EVENT_CLASS_TYPE(MouseMoved)
		EVENT_CLASS_CATEGORY(EventCategoryInput | EventCategoryMouse)

	private:
		float m_MouseX, m_MouseY;
	};

	class CIRCUITIZER_API MouseScrolledEvent : public Event
	{
	public:

		MouseScrolledEvent(float xOffset, float yOffset) : m_XOffset(xOffset), m_YOffset(yOffset)
		{
		}

		inline float GetXOffset() const { return m_XOffset; }
		inline float GetYOffset() const { return m_YOffset; }

		std::string ToString() const override
		{
			std::stringstream ss;
			ss << "MouseScrolledEvent: " << m_XOffset << ", " << m_YOffset;
			return ss.str;
		}

		EVENT_CLASS_TYPE(MouseScrolled)
		EVENT_CLASS_CATEGORY(EventCategoryInput | EventCategoryMouse)

	private:
		float m_XOffset, m_YOffset;
	};

	class CIRCUITIZER_API MouseButtonEvent : public Event
	{
	public:

		inline int GetMouseButton() const { return m_Button; }

		EVENT_CLASS_CATEGORY(EventCategoryInput | EventCategoryMouse)

	protected:
		MouseButtonEvent(int button) : m_Button(button)
		{
		}

		int m_Button;
	};

	class CIRCUITIZER_API MouseButtonPressedEvent : public MouseButtonEvent
	{
	public:
		MouseButtonPressedEvent(int button) : MouseButtonEvent(button)
		{
		}

		std::string ToString() const override
		{
			std::stringstream ss;
			ss << "MouseButtonPressedEvent: " << m_Button;
			return ss.str;
		}

		EVENT_CLASS_TYPE(MouseButtonPressed)
	};

	class CIRCUITIZER_API MosueButtonReleasedEvent : public MouseButtonEvent
	{
	public:
		MosueButtonReleasedEvent(int button) : MouseButtonEvent(button)
		{
		}

		std::string ToString() const override
		{
			std::stringstream ss;
			ss << "MosueButtonReleasedEvent: " << m_Button;
			return ss.str;
		}

		EVENT_CLASS_TYPE(MosueButtonReleased)
	};


}