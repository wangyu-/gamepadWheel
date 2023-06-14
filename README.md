# gamepadWheel
this project allows you:
1. simulate a racing wheel by using a gamepad, so that the game will recognize the gamepad as a wheel.  (so that you can bypass any steer assistant/limitations in game)
2. steer with gamepad in a way similar to how you steer with a racing wheel.  you steer by rotating the stick on your gamepad, and you can rotate beyond 360 degree.

# Usage

(on windows)

the script in the repo only works with xbox controller by default, but you should be able to modify it to support other gamepad with analog stick easily

1. Install [Vjoy](https://github.com/njz3/vJoy), [freePIE](https://github.com/AndersMalmgren/FreePIE) , [HidHide](https://github.com/ViGEm/HidHide). Reboot if required.
2. Open Vjoy configuration, make sure `Vjoy device 1` is enabled
3. Open freePIE, load the `gamepad_wheel.py` and run
4. Open HidHide to hide the xbox controller   (you need to do this to assign in-game axes/buttons correctly) (you only need to do this once)
5. open game, assign axes/buttons, and play
