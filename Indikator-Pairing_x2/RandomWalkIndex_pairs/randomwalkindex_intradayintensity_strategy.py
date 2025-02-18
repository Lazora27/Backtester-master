import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
