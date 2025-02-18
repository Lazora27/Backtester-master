import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AutoFibonacci': 1.0
        })
    )
