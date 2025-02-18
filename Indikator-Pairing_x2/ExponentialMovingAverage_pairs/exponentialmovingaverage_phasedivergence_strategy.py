import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'PhaseDivergence': 1.0
        })
    )
