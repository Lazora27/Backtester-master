import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PivotPoints': 1.0
        })
    )
