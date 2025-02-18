import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'IntradayIntensity': 1.0
        })
    )
