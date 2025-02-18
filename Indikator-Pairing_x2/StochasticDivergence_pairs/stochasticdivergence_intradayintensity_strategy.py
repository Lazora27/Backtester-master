import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'IntradayIntensity': 1.0
        })
    )
