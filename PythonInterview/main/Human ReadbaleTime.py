def format_seconds(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Input seconds must be a non-negative integer within the valid range.")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    # Format the components with zero-padding
    formatted_time = f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"

    return formatted_time

# Example usage:
seconds_input = 3668
formatted_time = format_seconds(seconds_input)
print(f"The human-readable format for {seconds_input} seconds is: {formatted_time}")
