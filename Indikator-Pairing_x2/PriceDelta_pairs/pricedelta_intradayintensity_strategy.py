import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'IntradayIntensity': 1.0
        })
    )
