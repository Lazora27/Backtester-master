import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ModifiedATR': 1.0
        })
    )
