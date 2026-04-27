<!-- SHOWCASE: false -->

# Remote-Controlled Vehicle

> A Raspberry Pi-based robot that combines keyboard-driven motor control with real-time sonar obstacle detection to drive a two-wheeled vehicle.

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Language](https://img.shields.io/badge/language-Python-blue)
![Semester](https://img.shields.io/badge/semester-Fall%202023-orange)

---

## Course Information

| Field                  | Details                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Course Title           | Introduction to Robotics                                                                                                                       |
| Course Number          | EGN 4060C                                                                                                                                      |
| Semester               | Fall 2023                                                                                                                                      |
| Assignment Title       | Remote-Controlled Vehicle                                                                                                                      |
| Assignment Description | Design and implement a remote-controlled robotic vehicle integrating motor control and sonar-based obstacle detection on an embedded platform. |

---

## Project Description

This project implements a keyboard-controlled robotic vehicle on a Raspberry Pi using GPIO-driven DC motors and an HC-SR04 ultrasonic distance sensor. The operator drives the vehicle using WASD keys via a terminal interface, with two speed modes available. An autonomous sonar mode (`t`) continuously reads distance to nearby obstacles and dynamically adjusts motor PWM duty cycle to maintain a safe following distance, stopping the vehicle when the 20-second run window expires.

---

## Screenshots / Demo

> _No screenshot available. Add one with: `![Demo](docs/your-image.png)`_

---

## Results

### Expected Terminal Output

**Manual Mode (`r` to enable, then WASD):**

```
    w-forward a-left s-backward d-right
    r-run c-stop Hold Shift to go faster
    Press e to cleanup before and after running
```

Each keypress prints the direction taken (e.g. `forward`, `left`) and the motors respond immediately.

**Autonomous Sonar Mode (`t`):**

```
Waiting for Sensor
PMW: 50 %   Timer: 0.1 sec   Distance: 24.35 cm   Previous Distance: 24.35 cm
PMW: 45 %   Timer: 0.2 sec   Distance: 19.80 cm   Previous Distance: 24.35 cm
PMW: 50 %   Timer: 0.3 sec   Distance: 24.10 cm   Previous Distance: 19.80 cm
```

Each line updates in-place (`\r`) during the 20-second run window (200 × 0.1s ticks).

| Field               | Meaning                                                      |
| ------------------- | ------------------------------------------------------------ |
| `PWM`               | Current motor duty cycle (0–100%). Higher = faster.          |
| `Timer`             | Elapsed seconds since sonar mode started. Stops at 20s.      |
| `Distance`          | Current measured distance to nearest obstacle in cm.         |
| `Previous Distance` | Distance reading from the prior tick, used to compute error. |

The controller increases PWM when the vehicle is moving away from an object (`error < -0.5 cm`) and decreases it when closing in (`error > 0.5 cm`), with a gain of 5% per tick. If output seems unresponsive, check `gainVal` and `pmwVal` initial values in `sonarMotorCombo.py`.

---

## Key Concepts

`GPIO Control` `PWM Motor Drive` `HC-SR04 Ultrasonic Sensor` `Proportional Control` `Raspberry Pi` `Embedded Python` `Real-Time Input Loop`

---

## Languages & Tools

- **Language:** Python 3
- **Library:** RPi.GPIO
- **Hardware:** Raspberry Pi, L298N Motor Driver, HC-SR04 Ultrasonic Sensor, DC Motors
- **Interface:** Terminal (stdin keyboard input)

---

## File Structure

```
project-root/
├── sonarMotorCombo.py    # Main script: motor control + sonar logic
├── requirements.txt      # Python dependencies
└── README.md
```

---

## Installation & Usage

### Prerequisites

- Raspberry Pi with GPIO header
- Python 3
- RPi.GPIO library

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/alexneilgreen/Intro-to-Robotics.git
cd Intro-to-Robotics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python sonarMotorCombo.py
```

### Controls

| Key | Action                               |
| --- | ------------------------------------ |
| `r` | Enable drive mode                    |
| `c` | Stop all motors                      |
| `w` | Forward                              |
| `s` | Backward                             |
| `a` | Turn left                            |
| `d` | Turn right                           |
| `h` | Toggle normal / fast speed           |
| `t` | Start autonomous sonar mode (20 sec) |
| `e` | GPIO cleanup and exit                |

> **Note:** Movement keys only respond when drive mode is active (`r` pressed first).

---

## Contributors

| Name               | Role                               | GitHub                                                             |
| ------------------ | ---------------------------------- | ------------------------------------------------------------------ |
| Alexander Green    | Development, Testing, Presentation | [@alexneilgreen](https://github.com/alexneilgreen)                 |
| Antonio Duchesneau | Development, Testing, Presentation | [@GitHubAccountExample1](https://github.com/GitHubAccountExample1) |
| Rodrigo Guerra     | Development, Testing, Presentation | [@GitHubAccountExample2](https://github.com/GitHubAccountExample2) |

---

## Academic Integrity

This repository is publicly available for **portfolio and reference purposes only**.
Please do not submit any part of this work as your own for academic coursework.
