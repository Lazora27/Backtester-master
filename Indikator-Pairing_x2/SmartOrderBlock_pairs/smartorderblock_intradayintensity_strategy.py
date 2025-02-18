import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'IntradayIntensity': 1.0
        })
    )
