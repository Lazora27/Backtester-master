import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MarketSentimentIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MarketSentimentIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MarketSentimentIndicator': 1.0
        })
    )
