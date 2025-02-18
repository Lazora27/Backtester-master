import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'IchimokuCloud': 1.0
        })
    )
