import asyncio

from cache_manager import CacheManager
from resource_manager import ResourceManager
from data_accessor import TrulyAwesomeBankAPIClient

async def main():
    cache_manager = CacheManager()
    truly_awesome_bank_API_client = TrulyAwesomeBankAPIClient()
    resource_manager = ResourceManager(cache_manager, truly_awesome_bank_API_client)

    transaction = {
        'type': 'PAYMENT',
        'amount': 100,
        'currency': 'EUR'
    }

    print('=======================')
    print('|    WRITE THROUGH    |')
    print('=======================')

    print('>>> Save transaction')
    entry = await resource_manager.save_with_write_through(transaction)
    print('>>> Get transaction')
    await resource_manager.fetch_transaction_by_id(entry['id'])

    print('=======================')
    print('|    WRITE BEHIND     |')
    print('=======================')

    print('>>> Save transaction')
    entry = await resource_manager.save_with_write_behind(transaction)
    print('>>> Get transaction')
    await resource_manager.fetch_transaction_by_id(entry['id'])

    print('')
    print('--------------------------------------------')
    print('|    AWESOME BANK DATABASE (before sync)   |')
    print('--------------------------------------------')
    print(truly_awesome_bank_API_client._TrulyAwesomeBankAPIClient__database)
    print('')

    # wait for synchronization 
    await asyncio.sleep(10)

    print('')
    print('--------------------------------------------')
    print('|    AWESOME BANK DATABASE (after sync)    |')
    print('--------------------------------------------')
    print(truly_awesome_bank_API_client._TrulyAwesomeBankAPIClient__database)
    print('')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()