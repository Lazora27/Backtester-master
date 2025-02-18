import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
