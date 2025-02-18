import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'PhaseDivergence': 1.0
        })
    )
