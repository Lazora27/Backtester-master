import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'MarketBalance': 1.0
        })
    )
