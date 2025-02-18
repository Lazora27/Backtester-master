import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
