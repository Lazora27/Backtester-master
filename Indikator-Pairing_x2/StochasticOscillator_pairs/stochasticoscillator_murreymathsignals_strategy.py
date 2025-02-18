import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
