import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ModifiedATR': 1.0
        })
    )
