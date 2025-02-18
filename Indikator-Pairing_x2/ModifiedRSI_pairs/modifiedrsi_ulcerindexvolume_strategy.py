import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
