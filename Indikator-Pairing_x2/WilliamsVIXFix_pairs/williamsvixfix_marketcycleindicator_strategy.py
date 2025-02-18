import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
