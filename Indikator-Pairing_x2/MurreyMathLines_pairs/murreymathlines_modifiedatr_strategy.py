import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'ModifiedATR': 1.0
        })
    )
