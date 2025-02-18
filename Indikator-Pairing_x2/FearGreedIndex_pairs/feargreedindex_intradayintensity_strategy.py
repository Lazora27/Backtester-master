import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
