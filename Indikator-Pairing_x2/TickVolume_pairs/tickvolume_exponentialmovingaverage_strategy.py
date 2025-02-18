import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
