import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'MarketBalance': 1.0
        })
    )
