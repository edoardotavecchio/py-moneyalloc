import tomllib
import sys
import math

def main():
    with open("rules.toml", mode="rb") as rules:
        rules = tomllib.load(rules)
    curvalue = float(sys.argv[1])

    # Beni rifugio
    safe_haven_isin = str(rules["safe_haven"]["isin"])
    safe_haven_amount = to_allocate(curvalue, rules["safe_haven"])
    print("Beni rifugio (" + safe_haven_isin + "): " + str(safe_haven_amount))

    # Obbligazioni statali
    bond_isin = str(rules["bond"]["isin"])
    bond_amount = to_allocate(curvalue, rules["bond"])
    print("Obbligazioni statali (" + bond_isin + "): " + str(bond_amount))

    #Stocks
    ##Totale
    stock_total_amount = round((curvalue/100)*rules["stock"]["percentage"], 2)
    print("Azionario totale: " + str(stock_total_amount))

    ##A distribuzione
    stock_distributed_isin = str(rules["stock_distributed"]["isin"])
    stock_distributed_amount = to_allocate(stock_total_amount, rules["stock_distributed"])
    print("Azionario a distribuzione (" + stock_distributed_isin + "): " + str(stock_distributed_amount))

    ##Ad accumulo
    stock_accumulating_isin = str(rules["stock_accumulating"]["isin"])
    stock_accumulating_amount = to_allocate(stock_total_amount, rules["stock_accumulating"])
    print("Azionario ad accumulo (" + stock_accumulating_isin + "): " + str(stock_accumulating_amount))

def to_allocate(total, config):
    return round(((total/100) * config["percentage"]) - config["allocated"], 2)

main()


