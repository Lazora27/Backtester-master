import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'TRIXIndicator': 1.0
        })
    )
