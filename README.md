# Game Condition Launcher

A simple GUI application built with Tkinter to launch programs or games based on certain conditions, including temporarily changing the system time.

## Features

- Browse and select executable files (.exe)
- Temporarily change system time to 2026-01-08 for launching
- Automatically restore original system time after launch
- User-friendly interface for launching applications

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)
- **Administrator privileges** (required for changing system time on Windows)

## Installation

1. Clone or download the repository.
2. Ensure Python is installed.
3. Run the application as administrator: Right-click on `GameConditionLauncher.py` and select "Run as administrator" or use `python GameConditionLauncher.py` in an elevated command prompt.

## Usage

1. Click "浏览..." (Browse) to select the program you want to run.
2. Click "启动程序（修改时间）" (Launch Program with Time Change) to temporarily set the date to 2026-01-08, launch the program, and restore the original time.

## Notes

- The system time is changed only briefly during the launch process.
- Ensure you have backup or synchronization for accurate time if needed.
- This tool is intended for testing or bypassing date-based restrictions in software.

## Future Enhancements

- Add condition checks before launching
- Support for multiple programs
- Configuration files for launch settings
- Custom date selection
