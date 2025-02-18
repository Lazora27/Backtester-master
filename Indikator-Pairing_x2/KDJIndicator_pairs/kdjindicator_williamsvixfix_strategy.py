import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
