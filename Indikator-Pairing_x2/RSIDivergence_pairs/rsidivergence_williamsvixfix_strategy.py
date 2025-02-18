import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
