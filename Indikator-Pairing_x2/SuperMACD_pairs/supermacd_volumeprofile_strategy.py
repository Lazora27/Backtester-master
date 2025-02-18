import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VolumeProfile': 1.0
        })
    )
