import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
