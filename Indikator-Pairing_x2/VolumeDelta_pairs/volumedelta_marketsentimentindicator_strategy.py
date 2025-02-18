import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
