import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
