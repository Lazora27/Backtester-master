import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und DemandIndex
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'DemandIndex': 1.0
        })
    )
