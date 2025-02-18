import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VolumeProfile': 1.0
        })
    )
