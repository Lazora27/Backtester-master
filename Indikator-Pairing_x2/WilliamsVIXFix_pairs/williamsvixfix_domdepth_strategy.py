import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DOMDepth
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DOMDepth': 1.0
        })
    )
