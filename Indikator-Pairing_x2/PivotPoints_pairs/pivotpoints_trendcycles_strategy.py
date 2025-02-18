import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'TrendCycles': 1.0
        })
    )
