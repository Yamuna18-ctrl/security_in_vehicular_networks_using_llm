def generate_event(msg):
    speed = msg["speed"]
    acc = msg["acceleration"]

    if acc < -2.5:
        return "Hard Braking Alert"

    elif speed > 33:
        return "Overspeed Warning"

    elif speed < 1:
        return "Vehicle Stopped"

    return "Normal Driving"
