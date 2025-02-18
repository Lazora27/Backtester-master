import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'OpenInterest': 1.0
        })
    )
