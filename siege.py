def parse(file):
    with open(file, 'r', encoding='utf-8') as f:
        next(f)
        next(f)
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            if line[0] != '[':
                print(f"Ошибочная строка: {line}")
                continue

            close_idx = line.find(']')
            if close_idx == -1:
                print(f"Ошибочная строка: {line}")
                continue

            tag = line[1:close_idx]
            rest = line[close_idx + 1:]

            if "[" in tag or "]" in tag:
                print(f"Ошибочная строка: {line}")
                continue

            fields = [p.strip() for p in rest.split('|')]
            if len(fields) < 3 or len(fields) > 4:
                print(f"Ошибочная строка: {line}")
                continue

            name = fields[0]

            try:
                damage = float(fields[1].replace(' ', '').replace(',', '.'))
            except ValueError:
                print(f"Ошибочная строка: {line}")
                continue

            weapon_status = 0.5
            if len(fields) > 2 and fields[2]:
                if fields[2].strip().lower() == "active":
                    weapon_status = 1.5
                else:
                    weapon_status = .5

            buffs = 0.
            if len(fields) > 3 and fields[3]:
                try:
                    buffs = float(fields[3].replace(' ', '').replace(',', '.'))
                except ValueError:
                    buffs = 0.

            total_damage = damage * weapon_status * (1. + .15 * buffs)

            print(f"Игрок {name} из гильдии {tag} нанес {total_damage:.2f} по воротам")


if __name__ == '__main__':
    parse("log.txt")
