import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
