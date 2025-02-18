import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
