import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'IntradayIntensity': 1.0
        })
    )
