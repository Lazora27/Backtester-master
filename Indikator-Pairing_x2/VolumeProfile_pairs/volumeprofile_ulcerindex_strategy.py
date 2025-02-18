import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'UlcerIndex': 1.0
        })
    )
