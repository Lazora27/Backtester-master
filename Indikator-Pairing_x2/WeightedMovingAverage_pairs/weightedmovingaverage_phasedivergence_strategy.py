import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'PhaseDivergence': 1.0
        })
    )
