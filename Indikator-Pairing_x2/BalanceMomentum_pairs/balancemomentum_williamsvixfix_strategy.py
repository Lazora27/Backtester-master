import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
