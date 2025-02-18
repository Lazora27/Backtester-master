import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ModifiedATR': 1.0
        })
    )
