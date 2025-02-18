import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
