import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
