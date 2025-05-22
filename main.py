from agents.data_collector import DataCollector
from agents.technical_analyst import TechnicalAnalyst
from agents.risk_manager import RiskManager
from agents.decision_maker import DecisionMaker
from agents.execution_agent import ExecutionAgent
import time
import logging
from datetime import datetime
import os
from dotenv import load_dotenv
import sys

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot.log'),
        logging.StreamHandler()
    ]
)

class TradingBot:
    def __init__(self, symbol: str, interval: str = '1h'):
        """
        Initialise le bot de trading
        
        Args:
            symbol (str): Paire de trading (ex: 'BTCUSDT')
            interval (str): Intervalle de temps pour les données
        """
        self.symbol = symbol
        self.interval = interval
        
        # Initialisation des agents
        self.data_collector = DataCollector()
        
    def run(self):
        print(self.data_collector)
        


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <symbol> <interval>")
        print("Example: python main.py BTCUSDT 1h")
        sys.exit(1)
        
    SYMBOL = sys.argv[1]
    INTERVAL = sys.argv[2]
    # Création et démarrage du bot
    bot = TradingBot(SYMBOL, INTERVAL)
    bot.run() 