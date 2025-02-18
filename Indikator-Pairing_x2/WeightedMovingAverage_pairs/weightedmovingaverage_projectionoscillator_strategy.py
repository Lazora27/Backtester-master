import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
