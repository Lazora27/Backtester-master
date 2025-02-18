import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
