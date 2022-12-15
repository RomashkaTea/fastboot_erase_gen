

erase_array = ["userdata", "system", "vendor", "boot", "cache", "recovery", "vbmeta", "misc", "abl", "modem", "modemst1", "modemst2", "fsg", "frp", "abl", "xblbak", "ablbak", "crclist", "sparsecrclist", "aboot", "bootloader", "xbl", "arb", "preloader", "aboot", "tz", "tzbak", "hyp", "hypbak", "rpm", "rpmbak", "devcfg", "devcfgbak", "cmnlib", "cmnlibbak", "cmnlib64", "cmnlib64bak", "dsp", "storsec", "storsecbak", "bluetooth", "keymaster", "keymasterbak", "logo", "splash"]
erase_ab_array = ["system", "vendor", "boot", "recovery", "product", "vbmeta", "vbmeta_system", "vbmeta_vendor"]
lock_bootloader = True

for i in erase_array:
    print(f"fastboot erase {i}")

for i in erase_ab_array:
    print(f"fastboot erase {i}_a")
    print(f"fastboot erase {i}_b")

if lock_bootloader:
    print("fastboot oem lock")
    print("fastboot flashing lock")
