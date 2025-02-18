import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PhaseDivergence': 1.0
        })
    )
