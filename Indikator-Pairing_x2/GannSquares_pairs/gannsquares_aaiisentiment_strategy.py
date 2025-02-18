import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AAIISentiment': 1.0
        })
    )
