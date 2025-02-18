import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
