import asyncio

async def chat_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print("=== Terhubung ke Async Server ===")
    print("Ketik pesan, ketik 'exit' untuk keluar\n")

    loop = asyncio.get_event_loop()

    try:
        while True:
            # Ambil input user tanpa memblokir event loop
            message = await loop.run_in_executor(None, input, "> ")

            if message.lower() == 'exit':
                print("Keluar dari chat...")
                break

            # Kirim ke server
            writer.write((message + "\n").encode())
            await writer.drain()

            # Terima balasan server
            response = await reader.read(100)
            if not response:
                print("Server menutup koneksi.")
                break

            print(response.decode().strip())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(chat_client())