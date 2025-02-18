import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'IntradayIntensity': 1.0
        })
    )
