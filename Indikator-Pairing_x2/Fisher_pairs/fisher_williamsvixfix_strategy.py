import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
