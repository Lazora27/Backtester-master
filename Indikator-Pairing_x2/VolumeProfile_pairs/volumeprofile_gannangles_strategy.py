import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und GannAngles
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'GannAngles': 1.0
        })
    )
