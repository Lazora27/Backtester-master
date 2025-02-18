import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'HilbertSinewave': 1.0
        })
    )
