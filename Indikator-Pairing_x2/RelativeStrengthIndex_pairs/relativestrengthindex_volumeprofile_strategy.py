import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
