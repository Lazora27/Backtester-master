import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'IntradayIntensity': 1.0
        })
    )
