import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'CumulativeTick': 1.0
        })
    )
