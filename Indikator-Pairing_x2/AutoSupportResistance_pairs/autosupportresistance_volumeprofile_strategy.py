import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'VolumeProfile': 1.0
        })
    )
