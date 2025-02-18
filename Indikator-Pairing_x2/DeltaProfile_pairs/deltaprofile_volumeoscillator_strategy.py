import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeOscillator': 1.0
        })
    )
