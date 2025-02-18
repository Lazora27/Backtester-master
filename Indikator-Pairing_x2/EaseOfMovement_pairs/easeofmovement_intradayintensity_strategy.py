import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'IntradayIntensity': 1.0
        })
    )
