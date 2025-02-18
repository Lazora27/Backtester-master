import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'PhaseDivergence': 1.0
        })
    )
