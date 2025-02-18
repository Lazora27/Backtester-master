import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'MarketBalance': 1.0
        })
    )
