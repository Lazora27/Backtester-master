import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'CoppockCurve': 1.0
        })
    )
