import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
