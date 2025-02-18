import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
