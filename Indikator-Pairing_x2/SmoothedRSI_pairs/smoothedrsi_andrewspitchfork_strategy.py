import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
