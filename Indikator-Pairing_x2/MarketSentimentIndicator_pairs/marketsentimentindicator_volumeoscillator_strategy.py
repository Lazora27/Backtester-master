import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketSentimentIndicator_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketSentimentIndicator und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MarketSentimentIndicator': {
                'class': MarketSentimentIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketSentimentIndicator'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MarketSentimentIndicator': 1.0,
            'VolumeOscillator': 1.0
        })
    )
