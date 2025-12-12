def main():
    with open("day11_input.txt") as f:
        devices = {}
        device_strs = f.read().splitlines()
        for device_str in device_strs:
            name = device_str[:3]
            outputs = device_str[5:].split()
            devices[name] = outputs
        f.close()

    def num_paths_from(device):
        if device == "out":
            return 1
        outputs = devices[device]
        num_paths = sum([num_paths_from(output) for output in outputs])
        return num_paths

    print(num_paths_from("you"))


if __name__ == "__main__":
    main()
