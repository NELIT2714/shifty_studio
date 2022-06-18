function findElements(object, element) {
	const instance = object;
	instance.element = element;
	instance.target = element.nextElementSibling;
}

function hideElement(object) {
	const instance = object
	const { target } = instance
    target.style.padding = null
    target.style.margin = null
	instance.isActive = false
    target.style.height = null
}

function showElement(object) {
	const instance = object;
	const { target, height } = instance
	target.style.height = `${height}px`
    target.style.padding = '25px 40px 25px 40px'
    target.style.margin = '0px 15px 20px 15px'
	instance.isActive = true
}

function changeElementStatus(instance) {
	if (instance.isActive) {
		hideElement(instance);
	} else {
		showElement(instance);
	}
}

function measureHeight(object) {
	const instance = object;
	instance.height = object.target.firstElementChild.clientHeight;
}

function subscribe(instance) {
	instance.element.addEventListener('click', (event) => {
		event.preventDefault();
		changeElementStatus(instance);
	});
	window.addEventListener('resize', () => measureHeight(instance));
}

function accordion(element) {
	const instance = {};
	function init() {
		findElements(instance, element);
		measureHeight(instance);
		subscribe(instance);
	}
	
	init();
}