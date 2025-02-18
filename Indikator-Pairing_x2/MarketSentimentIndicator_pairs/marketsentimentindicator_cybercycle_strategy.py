import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
