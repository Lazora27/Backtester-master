import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'IntradayIntensity': 1.0
        })
    )
