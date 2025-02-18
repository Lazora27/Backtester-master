import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
