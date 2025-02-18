import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedMovingAverage_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedMovingAverage und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'VolumeWeightedMovingAverage': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
