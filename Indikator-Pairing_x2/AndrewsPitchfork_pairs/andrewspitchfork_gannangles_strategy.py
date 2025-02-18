import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und GannAngles
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'GannAngles': 1.0
        })
    )
