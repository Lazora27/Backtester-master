import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'IntradayIntensity': 1.0
        })
    )
