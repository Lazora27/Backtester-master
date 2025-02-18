import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'MarketBalance': 1.0
        })
    )
