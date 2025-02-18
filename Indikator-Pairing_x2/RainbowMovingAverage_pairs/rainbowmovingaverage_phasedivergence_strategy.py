import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'PhaseDivergence': 1.0
        })
    )
