import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
