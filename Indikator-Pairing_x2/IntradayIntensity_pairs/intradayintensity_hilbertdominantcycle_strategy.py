import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
