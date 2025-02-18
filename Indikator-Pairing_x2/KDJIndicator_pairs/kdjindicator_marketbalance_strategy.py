import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
