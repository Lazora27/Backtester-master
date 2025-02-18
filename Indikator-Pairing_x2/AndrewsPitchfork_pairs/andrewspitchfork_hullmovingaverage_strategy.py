import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HullMovingAverage': 1.0
        })
    )
