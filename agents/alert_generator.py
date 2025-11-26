"""
Alert Generator Agent - Prioritized notification management
"""

import asyncio
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class AlertGeneratorAgent:
    """Generates prioritized alerts with recommendations"""

    def __init__(self):
        self.name = "alert_generator"
        logger.info(f"Initialized {self.name} agent")

    async def run(self, context: Dict[str, Any]) -> str:
        """Generate prioritized alerts"""
        try:
            alerts = context.get('alerts', [])

            report = "\n🚨 ALERT SUMMARY\n"
            report += "=" * 70 + "\n"

            if not alerts:
                report += "✅ No active alerts\n"
                report += "System Status: All nominal\n"
            else:
                for alert in alerts:
                    priority = alert.get('priority', 'INFO')
                    message = alert.get('message', '')

                    emoji = {'CRITICAL': '🔴', 'HIGH': '🟠', 'MEDIUM': '🟡', 'LOW': '🟢'}.get(priority, 'ℹ️')
                    report += f"{emoji} [{priority}] {message}\n"

            return report
        except Exception as e:
            logger.error(f"Alert generation failed: {e}")
            return f"❌ Error: Alert generation failed"
