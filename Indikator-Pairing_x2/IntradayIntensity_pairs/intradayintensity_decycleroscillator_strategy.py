import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
