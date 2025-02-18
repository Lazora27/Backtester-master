import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'UlcerIndex': 1.0
        })
    )
