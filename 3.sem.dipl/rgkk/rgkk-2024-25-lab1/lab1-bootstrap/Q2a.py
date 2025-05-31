from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Implementirajte `scriptPubKey` za zadatak 2
Q2a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 3652, OP_NUMEQUAL,
                         OP_DUP,OP_2SWAP, OP_SUB, 4588, OP_NUMEQUAL,
                         OP_VERIFY, OP_VERIFY
    
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # Postavite parametre transakcije
    # TODO: amount_to_send = {cjelokupni iznos BCY-a u UTXO-u kojeg saljemo} - {fee}
    amount_to_send = 0.000165 - 0.00001
    # TODO: Identifikator transakcije
    txid_to_spend = (
        '89ec5817e5496361f0e9d1c5fd1d560e33004b5c2bf4445243701a68a68469df')
    # TODO: indeks UTXO-a unutar transakcije na koju se referiramo
    # (indeksi pocinju od nula)
    utxo_index = 2
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
