import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'FlowOfFunds': 1.0
        })
    )
