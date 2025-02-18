import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'AverageLogRange': 1.0
        })
    )
