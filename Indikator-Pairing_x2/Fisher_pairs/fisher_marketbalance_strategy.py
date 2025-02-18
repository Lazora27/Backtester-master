import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MarketBalance
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MarketBalance': 1.0
        })
    )
