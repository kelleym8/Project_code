def wind_speed(u, v, w):
	"""Calculated wind speed from u, v, and w components."""
	return u * u + v * v + w * w

Woohoo I made a change!

hi


def get wind_direction(u, v):
	return 90 - atan2(u,v)