import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VolumeProfile': 1.0
        })
    )
