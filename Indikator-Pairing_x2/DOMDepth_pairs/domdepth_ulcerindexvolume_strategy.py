import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
