#!/use/bin/python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    for idx, person in enumerate(attendees, start=1):
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        final_text = (
            template.replace("{name}", str(name))
                .replace("{event_title}", str(event_title))
                .replace("{event_date}", str(event_date))
                .replace("{event_location}", str(event_location))
        )
        filename = f"output_{idx}.txt"

        try:
            with open(filename, "w") as file:
                file.write(final_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue