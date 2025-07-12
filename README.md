# AUDI-DECODE-SECRET-PIN

### Get your secret PIN and other info from your dump EEPROM file directly, without the need for any hardware or other software etc.

This project is created as part of the effort spent to populate my PIN code from my J518 module. This has been tested on J518 units running several software versions including 3.0 and 3.1, for 2KB EEPROM dumps from Motorola MC9S12 family (e.g., MC9S12DG128).

#### Features:

* Reads and decodes EEPROM binary dump
* Extracts VIN, PIN, Component Security bytes (CS1/CS2), MACs, Power Class
* Lists up to 4 stored EZS keys and key count
* WOrks on VAG cars between 2004 and 2012 (mostly)

#### No Need For:

* OBD tools
* Third-party commercial software
* Hardware

#### Sample (Anonymized) EEPROM Header:

```
00000000: 2468 1002 0010 fdb0 ffff 00ff 3736 3233  $h..........7623
00000010: 3933 3030 3231 3030 3131 ffff 3635 3233  9300210011..6523
00000020: 3833 3030 3031 3036 3031 ffff 3330 3436  8300010601..3046
00000030: 3330 3031 3330 3630 3033 3031 3331 3034  3001306003013104
00000040: 3432 3437 35ff ffff 3630 2e33 302e 3830  42475...60.30.80
00000050: 3233 3231 ffff ffff ffff ffff ffff ffff  2321............
00000060: ffff ffff ffff ffff 0308 3212 3446 3039  ..........2.4F09
00000070: 3130 3835 3220 2020 3032 3230 0001 0100  10852   0220....
00000080: 0783 a91e 7b26 3133 2e31 322e 3036 ffff  ....{&13.12.06..
00000090: 3446 3039 3035 3835 3242 2020 2033 31ff  4F0905852B   31.
```

---

For GUI version, we use Python and `tkinter` to allow drag-n-drop EEPROM decoding across platforms (Linux & Windows), with GitHub Actions pipeline that builds `.exe

For running GUI in linux:

```
python eeprom.decoder.j518.py
```

