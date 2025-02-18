import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TrueRange
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TrueRange': 1.0
        })
    )
