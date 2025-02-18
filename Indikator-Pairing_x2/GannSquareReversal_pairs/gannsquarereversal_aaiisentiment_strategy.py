import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AAIISentiment': 1.0
        })
    )
