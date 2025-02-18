import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ModifiedATR': 1.0
        })
    )
