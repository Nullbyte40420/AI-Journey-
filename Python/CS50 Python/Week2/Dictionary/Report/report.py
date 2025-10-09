def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"Distance": 163, "orbit": "Heliospheric"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ==============================
    ||                          ||
    ||     Spacecraft Report    ||
    ||                          ||
    ==============================
    Name: {spacecraft.get("name","Unknown")}
    Distance from Earth: {spacecraft.get("Distance","Unknown")} AU
    Orbit: {spacecraft.get("orbit","Unknown")}

    ==============================
    End of report

  """

main()