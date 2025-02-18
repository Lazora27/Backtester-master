import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ModifiedATR': 1.0
        })
    )
