import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'UlcerIndex': 1.0
        })
    )
