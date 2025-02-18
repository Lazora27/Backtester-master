import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedMovingAverage_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedMovingAverage und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedMovingAverage': {
                'class': VolumeWeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedMovingAverage'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeWeightedMovingAverage': 1.0,
            'CycleFinder': 1.0
        })
    )
