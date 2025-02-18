import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
