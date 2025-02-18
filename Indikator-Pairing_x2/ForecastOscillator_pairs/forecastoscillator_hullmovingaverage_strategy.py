import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'HullMovingAverage': 1.0
        })
    )
