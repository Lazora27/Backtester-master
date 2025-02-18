import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
