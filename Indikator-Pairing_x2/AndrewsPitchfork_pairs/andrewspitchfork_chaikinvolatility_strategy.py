import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
