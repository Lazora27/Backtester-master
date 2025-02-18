import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
