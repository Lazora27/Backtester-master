import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
