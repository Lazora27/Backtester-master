import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
