import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'VolatilityIndex': 1.0
        })
    )
