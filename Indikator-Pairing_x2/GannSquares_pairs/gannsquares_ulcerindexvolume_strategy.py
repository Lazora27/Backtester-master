import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
