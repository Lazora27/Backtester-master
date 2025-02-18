import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VolumeProfile': 1.0
        })
    )
