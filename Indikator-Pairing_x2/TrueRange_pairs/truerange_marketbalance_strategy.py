import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'MarketBalance': 1.0
        })
    )
