import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'IntradayIntensity': 1.0
        })
    )
