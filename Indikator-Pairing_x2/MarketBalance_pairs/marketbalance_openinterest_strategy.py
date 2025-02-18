import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'OpenInterest': 1.0
        })
    )
