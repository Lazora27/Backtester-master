import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
