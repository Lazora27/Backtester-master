import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
