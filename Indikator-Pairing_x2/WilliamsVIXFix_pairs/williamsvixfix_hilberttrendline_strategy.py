import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HilbertTrendline': 1.0
        })
    )
