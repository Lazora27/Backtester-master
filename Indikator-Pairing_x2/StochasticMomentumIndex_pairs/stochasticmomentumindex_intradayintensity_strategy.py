import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
