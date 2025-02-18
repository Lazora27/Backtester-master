import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'AverageTrueRange': 1.0
        })
    )
