from functools import cache


def main():
    with open("day11_input.txt") as f:
        devices = {}
        device_strs = f.read().splitlines()
        for device_str in device_strs:
            name = device_str[:3]
            outputs = device_str[5:].split()
            devices[name] = outputs
        f.close()

    @cache
    def num_paths_from(device, dac_passed, fft_passed):
        if device == "out":
            if dac_passed and fft_passed:
                return 1
            else:
                return 0
        outputs = devices[device]
        has_passed_dac = dac_passed
        has_passed_fft = fft_passed
        if device == "dac":
            has_passed_dac = True
        if device == "fft":
            has_passed_fft = True
        num_paths = sum([num_paths_from(output, has_passed_dac, has_passed_fft) for output in outputs])
        return num_paths

    print(num_paths_from("svr", False, False))


if __name__ == "__main__":
    main()
