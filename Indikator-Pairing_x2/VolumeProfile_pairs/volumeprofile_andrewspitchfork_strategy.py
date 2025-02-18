import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
