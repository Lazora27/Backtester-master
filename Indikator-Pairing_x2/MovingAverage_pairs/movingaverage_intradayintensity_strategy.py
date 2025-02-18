import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'IntradayIntensity': 1.0
        })
    )
