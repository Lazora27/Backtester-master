import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
