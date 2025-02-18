import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
