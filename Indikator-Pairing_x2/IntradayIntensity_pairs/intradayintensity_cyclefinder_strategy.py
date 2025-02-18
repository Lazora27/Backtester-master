import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und CycleFinder
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'CycleFinder': 1.0
        })
    )
