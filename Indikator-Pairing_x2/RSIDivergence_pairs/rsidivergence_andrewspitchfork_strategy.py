import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
