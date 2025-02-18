import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und OpenInterest
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'OpenInterest': 1.0
        })
    )
