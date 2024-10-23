from pq_solana_transfer_sdk.api import TransferClient

if __name__ == '__main__':
    transfer_cli = TransferClient()

    transfer_cli.endpoint = 'https://devnet.helius-rpc.com/?api-key=78065db3-87fb-431c-8d43-fcd190212125'

    transfer_cli.debug = True

    transfer_cli.payer_bs58_string = '2H8Gwy6xGMD76DhKfcPfh7gXkJfbUSduUc3aPVosxs54UFnJyijbDmh22iq2KYpPdMUUFDxS6iddxqtTJtWwinTn'

    sol_amount = 0.01

    receivers_address = ['D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK']

    transfer_cli.send_sol(receivers_list=receivers_address, amount=sol_amount)

    receivers_address = ['D27DgiipBR5dRdij2L6NQ27xwyiLK5Q2DsEM5ML5EuLK']
    mint = '8Q4SjHJYEFBQ9XC6rgiTnCJYi6JiHnVt8jXb6UqfP1KL'
    token_amount = 100
    transfer_cli.send_token(receivers_list=receivers_address, mint=mint, token_amount=token_amount)