import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MovingAverage
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MovingAverage': 1.0
        })
    )
