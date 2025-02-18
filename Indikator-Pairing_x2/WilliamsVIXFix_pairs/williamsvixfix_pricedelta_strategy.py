import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und PriceDelta
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'PriceDelta': 1.0
        })
    )
