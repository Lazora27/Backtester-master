import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalAdaptiveCycle_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalAdaptiveCycle und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FractalAdaptiveCycle': 1.0,
            'PhaseDivergence': 1.0
        })
    )
