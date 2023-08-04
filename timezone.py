from datetime import timedelta

def format_timezone(offset_seconds):
    # Convert the offset in seconds to a timedelta object
    offset_timedelta = timedelta(seconds=offset_seconds)

    # Get the sign of the offset (+ or -)
    sign = "+" if offset_timedelta >= timedelta(0) else "-"

    # Get the absolute value of the offset
    offset_timedelta = abs(offset_timedelta)

    # Extract hours and minutes from the timedelta object
    hours, remainder = divmod(offset_timedelta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Format the output as +/-HH:MM
    formatted_timezone = f"{sign}{hours:02d}:{minutes:02d}"

    return formatted_timezone

