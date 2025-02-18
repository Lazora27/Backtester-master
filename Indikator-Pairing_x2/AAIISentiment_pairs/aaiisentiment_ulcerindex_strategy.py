import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'UlcerIndex': 1.0
        })
    )
