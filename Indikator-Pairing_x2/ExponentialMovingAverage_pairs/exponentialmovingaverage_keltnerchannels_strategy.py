import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'KeltnerChannels': 1.0
        })
    )
