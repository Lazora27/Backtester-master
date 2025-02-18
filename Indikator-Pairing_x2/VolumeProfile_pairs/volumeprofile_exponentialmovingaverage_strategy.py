import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
