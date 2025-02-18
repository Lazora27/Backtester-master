import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'IntradayIntensity': 1.0
        })
    )
