import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeProfile': 1.0
        })
    )
