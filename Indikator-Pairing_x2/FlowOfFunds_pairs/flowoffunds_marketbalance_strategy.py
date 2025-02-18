import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'MarketBalance': 1.0
        })
    )
