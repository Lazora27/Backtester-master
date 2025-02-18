import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
