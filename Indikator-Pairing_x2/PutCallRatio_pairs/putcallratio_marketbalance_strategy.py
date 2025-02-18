import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MarketBalance
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MarketBalance': 1.0
        })
    )
