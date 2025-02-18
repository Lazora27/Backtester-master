import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'IntradayIntensity': 1.0
        })
    )
