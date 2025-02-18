import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
