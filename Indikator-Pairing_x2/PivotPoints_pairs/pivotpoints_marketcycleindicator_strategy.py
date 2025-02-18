import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
