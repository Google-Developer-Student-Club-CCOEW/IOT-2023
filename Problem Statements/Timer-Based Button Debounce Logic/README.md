Problem Statement - Implement button debounce logic which is an alternative to the traditional time-based approach.

Description - Traditional Debounce logic follows the route that
if(currentTime - lastTime > debounceTime) {
	button press is registered
}

This logic brings with it drawbacks such as
1. If user holds the button for time more than debounceTime, another press is registered.

To tackle this issue create a debounce logic that does not require any time/timer based metric. 
