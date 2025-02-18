import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'VolumeProfile': 1.0
        })
    )
