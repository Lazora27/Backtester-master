import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'StochasticRSI': 1.0
        })
    )
