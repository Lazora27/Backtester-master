import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
