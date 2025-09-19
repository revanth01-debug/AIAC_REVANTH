from datetime import datetime
from typing import List, Dict, Any

def calculate_average_ticket_duration(tickets: List[Dict[str, Any]]) -> int:
    """
    Computes the average duration in minutes between ticket 'opened' and 'closed' timestamps.

    This function iterates through a list of tickets, parsing the 'opened' and
    'closed' timestamps for each. It calculates the duration in minutes for each
    valid ticket and then returns the average.

    Args:
        tickets (List[Dict[str, Any]]): A list of dictionaries, where each
            dictionary represents a ticket. Each ticket should contain 'opened'
            and 'closed' keys with ISO 8601 formatted timestamp strings
            (e.g., '2023-10-27T10:00:00').

    Returns:
        int: The average duration in minutes (truncated). Returns 0 if no
             valid tickets with both 'opened' and 'closed' timestamps are found.
    """
    total_minutes = 0.0
    valid_ticket_count = 0

    for ticket in tickets:
        try:
            opened_time = datetime.fromisoformat(ticket['opened'])
            closed_time = datetime.fromisoformat(ticket['closed'])

            duration = closed_time - opened_time
            total_minutes += duration.total_seconds() / 60
            valid_ticket_count += 1
        except (KeyError, ValueError, TypeError):
            # Skip any tickets that are missing keys or have invalid timestamp formats.
            continue

    if valid_ticket_count == 0:
        return 0

    return int(total_minutes / valid_ticket_count)


if _name_ == "_main_":
    sample_tickets = [
        {'opened': '2023-10-27T10:00:00', 'closed': '2023-10-27T10:45:00'},  # 45 mins
        {'opened': '2023-10-27T11:00:00', 'closed': '2023-10-27T12:30:00'},  # 90 mins
        {'opened': '2023-10-27T13:00:00'},  # Invalid: missing 'closed' key
        {'opened': 'invalid-date', 'closed': '2023-10-27T15:00:00'},      # Invalid: bad format
    ]

    average_duration = calculate_average_ticket_duration(sample_tickets)
    print(f"Average ticket resolution time: {average_duration} minutes")
    assert average_duration == 67, "Test failed: Calculation is incorrect"
    print("Test passed successfully! ✅")