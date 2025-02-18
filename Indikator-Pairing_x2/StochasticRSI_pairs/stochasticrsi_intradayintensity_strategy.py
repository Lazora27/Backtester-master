import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'IntradayIntensity': 1.0
        })
    )
