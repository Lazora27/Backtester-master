import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'IntradayIntensity': 1.0
        })
    )
