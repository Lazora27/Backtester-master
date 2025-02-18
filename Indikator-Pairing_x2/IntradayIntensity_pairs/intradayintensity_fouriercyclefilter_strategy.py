import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
