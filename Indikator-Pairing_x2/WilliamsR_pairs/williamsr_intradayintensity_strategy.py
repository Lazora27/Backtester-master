import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'IntradayIntensity': 1.0
        })
    )
