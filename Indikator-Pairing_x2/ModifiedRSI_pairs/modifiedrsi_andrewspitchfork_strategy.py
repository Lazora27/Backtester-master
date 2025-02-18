import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
