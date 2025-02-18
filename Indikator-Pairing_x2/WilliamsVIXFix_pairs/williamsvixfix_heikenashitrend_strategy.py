import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
