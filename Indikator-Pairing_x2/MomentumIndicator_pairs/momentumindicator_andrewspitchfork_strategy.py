import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
