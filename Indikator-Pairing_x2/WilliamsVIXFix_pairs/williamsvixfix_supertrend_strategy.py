import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SuperTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SuperTrend': 1.0
        })
    )
