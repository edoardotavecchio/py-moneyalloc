import tomllib
import sys

def main():
    with open("rules.toml", mode="rb") as rules:
        rules = tomllib.load(rules)
    curvalue = float(sys.argv[1])

    print_allocated(rules)

    for asset in rules['asset']:
        if 'subtype' in asset:
            type_amount = to_allocate(curvalue, asset)
            for subtype in asset['subtype']:
                isin = str(subtype['isin'])
                amount = to_allocate(type_amount, subtype)
                print(asset['type'] + '.' + subtype['type'] + ' (' + isin + '): ' + str(amount) + "€")
            continue
        isin = str(asset['isin'])
        amount = to_allocate(curvalue, asset)
        print(asset['type'] + ' (' + isin + '): ' + str(amount) + "€")


def to_allocate(total, config):
    if 'allocated' in config:
        return round(((total/100) * config["percentage"]) - config["allocated"], 2)
    else:
        return round(((total/100) * config["percentage"]), 2)

def print_allocated(rules):
    print("Hai indicato i seguenti valori come già allocati:")
    for asset in rules['asset']:
        if 'subtype' in asset:
            for subtype in asset['subtype']:
                print(asset['type'] + '.' + subtype['type'] + ': ' + str(subtype['allocated']) + "€")
            continue
        print(asset['type'] + ': ' + str(asset['allocated']) + "€")
    print("Se vuoi sovrascriverne alcuni, modifica il file rules.toml.")
    stop = input("Vuoi fermare l'esecuzione per modificare? (y/N)")
    if stop == 'y':
        sys.exit()
    print('----------------------------------------------------------------------')

main()


