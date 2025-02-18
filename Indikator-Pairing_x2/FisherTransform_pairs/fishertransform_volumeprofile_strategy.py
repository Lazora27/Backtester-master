import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VolumeProfile': 1.0
        })
    )
