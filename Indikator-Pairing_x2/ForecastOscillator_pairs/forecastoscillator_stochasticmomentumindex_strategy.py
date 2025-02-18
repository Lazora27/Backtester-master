import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
