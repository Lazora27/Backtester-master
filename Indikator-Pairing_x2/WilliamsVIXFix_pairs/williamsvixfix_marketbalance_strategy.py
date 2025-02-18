import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MarketBalance
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MarketBalance': 1.0
        })
    )
