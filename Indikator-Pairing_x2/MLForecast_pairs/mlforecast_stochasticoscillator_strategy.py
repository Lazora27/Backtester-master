import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'StochasticOscillator': 1.0
        })
    )
