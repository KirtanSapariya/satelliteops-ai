"""
SatelliteOps AI - Main Entry Point
Multi-Agent System for Autonomous Satellite Operations

Author: Kirtan Sapariya
Date: November 2025
Competition: Kaggle AI Agents Intensive Capstone Project
"""

import asyncio
import os
from dotenv import load_dotenv
from agents.mission_coordinator import create_mission_coordinator
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

async def main():
    """Main entry point for SatelliteOps AI system"""

    print("="*80)
    print("🛰️  SATELLITEOPS AI - Autonomous Satellite Operations System")
    print("="*80)
    print("\nInitializing multi-agent system...\n")

    # Verify API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        logger.error("GOOGLE_API_KEY not found in environment variables")
        print("❌ Error: Please set GOOGLE_API_KEY in .env file")
        return

    try:
        # Create mission coordinator agent
        logger.info("Creating mission coordinator agent...")
        coordinator = await create_mission_coordinator()

        print("✅ System initialized successfully!\n")
        print("="*80)
        print("Available Commands:")
        print("  1. 'status' - Show constellation status")
        print("  2. 'anomaly' - Detect anomalies in telemetry")
        print("  3. 'orbit' - Predict orbital trajectories")
        print("  4. 'collision' - Check collision risks")
        print("  5. 'report' - Generate mission report")
        print("  6. 'help' - Show this menu")
        print("  7. 'exit' - Exit system")
        print("  Or type any natural language query!")
        print("="*80)

        # Interactive loop
        while True:
            try:
                user_input = input("\n🛰️  Query: ").strip()

                if not user_input:
                    continue

                if user_input.lower() == 'exit':
                    print("\n👋 Shutting down SatelliteOps AI...")
                    break

                if user_input.lower() == 'help':
                    print("\nAvailable Commands:")
                    print("  • status - Show all satellites status")
                    print("  • anomaly - Run anomaly detection")
                    print("  • orbit - Predict next 24 hours")
                    print("  • collision - Check conjunction risks")
                    print("  • report - Generate comprehensive report")
                    continue

                # Process query through mission coordinator
                print("\n🤖 Processing query...\n")
                response = await coordinator.run(user_input)

                print(f"\n📊 Response:\n{response}")

            except KeyboardInterrupt:
                print("\n\n👋 Shutting down SatelliteOps AI...")
                break
            except Exception as e:
                logger.error(f"Error processing query: {e}")
                print(f"\n❌ Error: {e}")
                print("Please try again or type 'help' for available commands.")

    except Exception as e:
        logger.error(f"System initialization failed: {e}")
        print(f"\n❌ Fatal Error: {e}")
        return

    print("\n✅ System shutdown complete.")

if __name__ == "__main__":
    asyncio.run(main())
