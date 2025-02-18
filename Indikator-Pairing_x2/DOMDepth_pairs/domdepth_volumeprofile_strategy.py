import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolumeProfile': 1.0
        })
    )
