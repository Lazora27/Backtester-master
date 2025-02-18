import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
