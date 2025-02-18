import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VolumeProfile': 1.0
        })
    )
