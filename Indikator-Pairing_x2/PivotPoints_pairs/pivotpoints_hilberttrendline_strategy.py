import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HilbertTrendline': 1.0
        })
    )
