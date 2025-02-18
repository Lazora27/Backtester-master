import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PivotPoints
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PivotPoints': 1.0
        })
    )
