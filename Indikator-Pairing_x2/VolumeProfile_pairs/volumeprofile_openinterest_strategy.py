import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und OpenInterest
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'OpenInterest': 1.0
        })
    )
