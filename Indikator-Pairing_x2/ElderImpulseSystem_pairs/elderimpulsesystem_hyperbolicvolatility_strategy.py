import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
