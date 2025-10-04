# Getting Your Code onto the Raspberry Pi Pico

The easiest way to get your `main.py` file onto the Raspberry Pi Pico is by using a free program called **Thonny IDE**. It handles both the initial setup and saving files to the device in a few simple steps.

---

## 👩‍💻 Phase 1: First-Time Setup (Installing MicroPython)

> **Note:** If you've never used your Pico before, you first need to install the MicroPython firmware. You only need to do this once.

### 1. Install Thonny IDE
Download and install Thonny from its official website: thonny.org.

### 2. Put the Pico in BOOTSEL Mode
1.  Unplug your Pico from the computer.
2.  Press and hold the small white **`BOOTSEL`** button on the Pico.
3.  While still holding the button, plug the Pico into your computer's USB port.
4.  Release the **`BOOTSEL`** button.
5.  Your computer will detect the Pico as a small USB drive named `RPI-RP2`.

### 3. Install the Firmware with Thonny
1.  Open Thonny.
2.  Go to the menu and select **Tools -> Options**.
3.  Click on the **Interpreter** tab.
4.  Select `"MicroPython (Raspberry Pi Pico)"` as the interpreter.
5.  Below the port selection, click the **"Install or update firmware"** link.
6.  Click **Install**. Thonny will automatically download and install the latest MicroPython firmware onto your Pico.
7.  When it's done, close the dialogs. The Pico will reboot, and Thonny's "Shell" panel should now show a MicroPython prompt.

---

## 💾 Phase 2: Copying Your `main.py` File

Now that MicroPython is running, you can save your script to the Pico.

### 1. Save the File to the Pico
1.  Paste your final Python code into the main editor window in Thonny.
2.  Go to the menu and select **File -> Save as...**.
3.  A window will pop up asking where to save the file. Choose **"Raspberry Pi Pico"**.
4.  In the next window, for the filename, type exactly: `main.py`
5.  Click **OK**.

### 2. Test It ✅
That's it! The file is now on your Pico. To test that it runs automatically, simply unplug the Pico from your computer and then plug it back in. It will not show up as a drive this time; it will just start running the code saved in your `main.py` file.