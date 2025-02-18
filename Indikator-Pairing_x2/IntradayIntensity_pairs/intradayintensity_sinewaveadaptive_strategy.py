import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
