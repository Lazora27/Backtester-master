import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und MarketBalance
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'MarketBalance': 1.0
        })
    )
