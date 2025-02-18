import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'CycleFinder': 1.0
        })
    )
