import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
