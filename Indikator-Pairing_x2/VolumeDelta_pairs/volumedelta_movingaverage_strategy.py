import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MovingAverage': 1.0
        })
    )
