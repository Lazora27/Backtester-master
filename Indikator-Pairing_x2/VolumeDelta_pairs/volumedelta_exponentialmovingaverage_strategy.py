import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
