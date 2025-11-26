import asyncio
from agents.mission_coordinator import create_mission_coordinator

async def run_all_commands():
    coordinator = await create_mission_coordinator()
    commands = ['status', 'anomaly', 'orbit', 'collision', 'report', 'help', 'exit']

    for cmd in commands:
        print(f"\n🛰️ Query: {cmd}\n")
        if cmd == 'exit':
            print("Exiting...\n")
            break
        response = await coordinator.run(cmd)
        print("🤖 Response:\n")
        print(response)

if __name__ == '__main__':
    asyncio.run(run_all_commands())
