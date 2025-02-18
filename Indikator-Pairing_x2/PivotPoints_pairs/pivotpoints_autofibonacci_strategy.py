import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AutoFibonacci': 1.0
        })
    )
