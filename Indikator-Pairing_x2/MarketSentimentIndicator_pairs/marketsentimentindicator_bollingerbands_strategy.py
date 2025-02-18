import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
