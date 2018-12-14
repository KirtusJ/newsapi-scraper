try:
	from . import setup, constants, auth
except ImportError as IE:
	print(f"Error importing: {IE}")