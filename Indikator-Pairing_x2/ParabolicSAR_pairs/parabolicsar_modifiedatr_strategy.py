import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'ModifiedATR': 1.0
        })
    )
