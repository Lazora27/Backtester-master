import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AAIISentiment': 1.0
        })
    )
