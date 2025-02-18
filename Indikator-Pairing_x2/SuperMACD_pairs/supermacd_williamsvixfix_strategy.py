import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
