import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
