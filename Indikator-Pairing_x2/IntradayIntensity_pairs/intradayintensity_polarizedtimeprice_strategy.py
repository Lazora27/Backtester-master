import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
