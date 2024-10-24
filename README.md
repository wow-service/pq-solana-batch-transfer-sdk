## 依赖库功能介绍

```
solana批量转账/批量转token
```

## 安装(install)

```
pip install pq-solana-transfer-sdk
```

## 使用说明

```
# 实例化对象
cli = TransferClient()

# 指定rpc, 默认为开发网endpoint
cli.endpoint = 'rpc endpoint'
# 指定钱包私钥
cli.payer_bs58_string = "bs58私钥字符串"
# 开启控制台打印信息，默认为False
cli.debug = True


TransferClient类有两个方法

注: 最大转账地址数量(15)

## 方法一: 批量发送sol
send_sol(self, receivers_list=None, amount=0.0)

	1.1 receivers_list 
		接收者列表
	1.2 amount
		发送sol数量

## 方法二: 批量发送spl-token
send_token(self, receivers_list=None, mint='', token_amount=0.0, instruction_params=None)

	1.1 receivers_list 
		接收者列表
	1.2 mint
		token地址
	1.3 token_amount
		发送token数量
	1.4 instruction_params
		参数格式为:
            instruction_params = {
                'token_program_id': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA',
                'token_decimals': 9
            }
        如需更改请自行传入
```

