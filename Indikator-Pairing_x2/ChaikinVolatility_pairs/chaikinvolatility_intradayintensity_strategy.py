import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'IntradayIntensity': 1.0
        })
    )
