import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
