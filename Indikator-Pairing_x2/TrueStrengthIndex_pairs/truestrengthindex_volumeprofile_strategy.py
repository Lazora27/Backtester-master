import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
