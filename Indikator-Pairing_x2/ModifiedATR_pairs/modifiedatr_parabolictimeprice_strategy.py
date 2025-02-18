import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
