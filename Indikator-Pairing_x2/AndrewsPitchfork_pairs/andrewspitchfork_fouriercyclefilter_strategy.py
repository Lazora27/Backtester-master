import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
