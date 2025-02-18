import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
