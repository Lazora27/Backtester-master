import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
