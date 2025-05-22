from binance.client import Client
from datetime import datetime
import pandas as pd
import os
from dotenv import load_dotenv

class DataCollector:
    def __init__(self):
        load_dotenv()
        self.client = Client(
            os.getenv('BINANCE_API_KEY'),
            os.getenv('BINANCE_API_SECRET')
        )
        
    def get_historical_klines(self, symbol: str, interval: str, start_str: str, end_str: str = None) -> pd.DataFrame:
        """
        Récupère les données historiques pour un symbole donné
        
        Args:
            symbol (str): Paire de trading (ex: 'BTCUSDT')
            interval (str): Intervalle de temps (ex: '1h', '4h', '1d')
            start_str (str): Date de début
            end_str (str, optional): Date de fin. Defaults to None.
            
        Returns:
            pd.DataFrame: DataFrame contenant les données OHLCV
        """
        klines = self.client.get_historical_klines(
            symbol=symbol,
            interval=interval,
            start_str=start_str,
            end_str=end_str
        )
        
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ])
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        
        # Conversion des colonnes en float
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
            
        return df
    
    def get_current_price(self, symbol: str) -> float:
        """
        Récupère le prix actuel d'un symbole
        
        Args:
            symbol (str): Paire de trading (ex: 'BTCUSDT')
            
        Returns:
            float: Prix actuel
        """
        ticker = self.client.get_symbol_ticker(symbol=symbol)
        return float(ticker['price'])
    
    def get_market_depth(self, symbol: str, limit: int = 100) -> dict:
        """
        Récupère la profondeur du marché pour un symbole
        
        Args:
            symbol (str): Paire de trading (ex: 'BTCUSDT')
            limit (int, optional): Nombre d'ordres à récupérer. Defaults to 100.
            
        Returns:
            dict: Dictionnaire contenant les ordres d'achat et de vente
        """
        depth = self.client.get_order_book(symbol=symbol, limit=limit)
        return {
            'bids': depth['bids'],
            'asks': depth['asks']
        } 