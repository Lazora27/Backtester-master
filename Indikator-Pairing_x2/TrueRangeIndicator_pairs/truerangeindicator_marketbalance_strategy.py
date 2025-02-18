import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
