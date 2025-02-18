import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
