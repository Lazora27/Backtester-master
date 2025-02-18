import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
