import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und TimeCycle
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'TimeCycle': 1.0
        })
    )
