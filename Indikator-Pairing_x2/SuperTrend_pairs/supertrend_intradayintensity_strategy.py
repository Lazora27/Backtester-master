import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'IntradayIntensity': 1.0
        })
    )
