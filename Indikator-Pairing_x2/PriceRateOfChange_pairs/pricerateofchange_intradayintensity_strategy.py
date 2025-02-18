import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'IntradayIntensity': 1.0
        })
    )
