import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
