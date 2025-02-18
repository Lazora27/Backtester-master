import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und GannFans
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'GannFans': 1.0
        })
    )
