import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VolumeProfile': 1.0
        })
    )
