import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ModifiedATR': 1.0
        })
    )
