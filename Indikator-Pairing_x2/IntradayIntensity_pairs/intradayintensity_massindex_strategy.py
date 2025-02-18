import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und MassIndex
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'MassIndex': 1.0
        })
    )
