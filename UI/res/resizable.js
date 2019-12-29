/*Make resizable div by Hung Nguyen*/
function makeResizablePanel(div)
{
	const element = document.querySelector(div);
	const resizers = document.querySelectorAll(div + ' .resizer')
	const minimum_size = 20;
	let original_width = 0;
	let original_x = 0;
	let original_mouse_x = 0;
	for (let i = 0; i < resizers.length; i++)
	{
		const currentResizer = resizers[i];
		currentResizer.addEventListener('mousedown', function (e)
		{
			e.preventDefault()
			original_width = parseFloat(getComputedStyle(element, null).getPropertyValue('width').replace('px', ''));
			original_x = element.getBoundingClientRect().left;
			original_mouse_x = e.pageX;
			window.addEventListener('mousemove', resize)
			window.addEventListener('mouseup', stopResize)
		})

		function resize(e)
		{
			if (currentResizer.classList.contains('bottom-right'))
			{
				const width = original_width + (e.pageX - original_mouse_x);
				if (width > minimum_size)
				{
					element.style.width = width + 'px'
				}
			}
			else if (currentResizer.classList.contains('bottom-left'))
			{
				const width = original_width - (e.pageX - original_mouse_x)
				if (width > minimum_size)
				{
					element.style.width = width + 'px'
					element.style.left = original_x + (e.pageX - original_mouse_x) + 'px'
				}
			}
			else if (currentResizer.classList.contains('top-right'))
			{
				const width = original_width + (e.pageX - original_mouse_x)
				if (width > minimum_size)
				{
					element.style.width = width + 'px'
				}
			}
			else
			{
				const width = original_width - (e.pageX - original_mouse_x)
				if (width > minimum_size)
				{
					element.style.width = width + 'px'
					element.style.left = original_x + (e.pageX - original_mouse_x) + 'px'
				}
			}
		}

		function stopResize()
		{
			window.removeEventListener('mousemove', resize)
		}
	}
}

makeResizablePanel('.resizable')
