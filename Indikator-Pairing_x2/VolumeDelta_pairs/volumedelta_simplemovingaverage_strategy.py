import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
