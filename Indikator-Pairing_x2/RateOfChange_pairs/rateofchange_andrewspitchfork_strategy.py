import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
