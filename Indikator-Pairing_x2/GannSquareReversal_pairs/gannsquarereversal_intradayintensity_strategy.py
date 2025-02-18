import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'IntradayIntensity': 1.0
        })
    )
