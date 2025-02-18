import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'VolumeOscillator': 1.0
        })
    )
