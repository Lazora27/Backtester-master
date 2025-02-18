import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'TrendCycles': 1.0
        })
    )
