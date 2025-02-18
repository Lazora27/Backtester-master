import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
