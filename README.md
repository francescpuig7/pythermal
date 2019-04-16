# pythermal
Impresión en impresoras térmicas

Simply execute: `python easy_print.py`

## On Windows

- Show device properties:

![Capturas](https://user-images.githubusercontent.com/19941550/56249480-3321b800-60ac-11e9-99ae-bfe335e2ea16.PNG)

- Install [zadig](https://zadig.akeo.ie/) if the `usb.core.NoBackendError: No backend available` raises

![capt](https://user-images.githubusercontent.com/19941550/56249390-dd4d1000-60ab-11e9-9e26-63796df4ff30.PNG)

## On Unix
Inspect:

```bash
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 004: ID 0421:01c7 Nokia Mobile Phones
Bus 001 Device 003: ID 0bda:8187 Realtek Semiconductor Corp. RTL8187 Wireless Adapter
Bus 001 Device 005: ID 0e21:0750 Cowon Systems, Inc.
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 006 Device 002: ID 046d:c01b Logitech, Inc. MX310 Optical Mouse
Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 008 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
```

Enjoy!
