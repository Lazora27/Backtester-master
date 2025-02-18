import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'WeeklyCycle': 1.0
        })
    )
