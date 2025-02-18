import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'IntradayIntensity': 1.0
        })
    )
