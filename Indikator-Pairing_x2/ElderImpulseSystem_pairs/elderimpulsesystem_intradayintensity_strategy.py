import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'IntradayIntensity': 1.0
        })
    )
