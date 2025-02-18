import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'IntradayIntensity': 1.0
        })
    )
