# CAPTCHA
Computer Access Protection through Triggered Camera &amp; Human Analysis
---
A program to automatically capture whoever opened your PC.

How to use (Windows):
 * Press Win + R, type `taskschd.msc` and press Enter.
 * In the right sidebar, click "Create Task".
 * On the General tab, give it a name (in this case "CAPTCHA")
 * Go to the Triggers tab, click New..., and set Begin the task: to On workstation unlock.
 * Go to the Actions tab, click New..., set Program/script: to the `captcha.exe` file directory. And set Start in: to the folder directory of where the `captcha.exe` file is. (IMPORTANT: set the directory to the folder of the file, NOT the directory to the file itself.)
 * Go to the Conditions tab and uncheck "Start the task only if the computer is on AC power" (Optional, if you don't have a battery, this is fine)
 * Test it by locking your PC (Win + L) and unlocking it. The captured images will be in `/captures`

> For Mac users, you can use the source code to turn it into a `.app` file.
