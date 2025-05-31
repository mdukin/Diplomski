from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                        faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


# TODO: Generirajte privatne kljuceve od klijenata koristeci `lib/keygen.py`
# i dodajte ih ovdje.
cust1_private_key = CBitcoinSecret(
    'cUDmuuBUg76Fm5qqBoh5C5MvPBjFJHENj9S5sVxgqPe4yifvYwGR')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cURGfHt38wPNp6xXzvQ8YW8Wwb9NMU3xwY1BDk3LxHHkMfjiwbMe')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cNkgM8eDTP8dCsqRCyVXeRubScH3oBiSypanG3yo2egrm7Z6UgWS')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Implementirajte `scriptPubKey` za zadatak 3

# Pretpostavite da vi igrate ulogu banke u ovom zadatku na nacin da privatni
# kljuc od banke `bank_private_key` odgovara vasem privatnom kljucu
# `my_private_key`.

Q3a_txout_scriptPubKey = [
        OP_3DUP,
        OP_3DUP,
        2,          
        my_public_key,                      
        cust1_public_key,          
        2,                   
        OP_CHECKMULTISIG,
        OP_NOTIF,
            2,          
            my_public_key,                       
            cust2_public_key,  
            2,                   
            OP_CHECKMULTISIG,
            OP_NOTIF,
                2,          
                my_public_key,                      
                cust3_public_key,       
                2,                   
                OP_CHECKMULTISIG,
            OP_ENDIF,
        OP_ENDIF,

]

######################################################################

if __name__ == '__main__':
    ######################################################################
    # Postavite parametre transakcije
    # TODO: amount_to_send = {cjelokupni iznos BCY-a u UTXO-u kojeg otkljucavamo} - {fee}
    amount_to_send = 0.0000155 - 0.00001
    # TODO: Identifikator transakcije
    txid_to_spend = (
        'e4b651714b551b32750ddb3c5f55f5d9fa5aada9edca897e73d4e454619c50c7')
    # TODO: indeks UTXO-a unutar transakcije na koju se referiramo
    # (indeksi pocinju od nula)
    utxo_index = 3
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend,
                                           utxo_index, Q3a_txout_scriptPubKey,
                                           my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
