import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
