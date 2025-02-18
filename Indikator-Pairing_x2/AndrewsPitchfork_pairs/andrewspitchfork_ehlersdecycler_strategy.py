import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'EhlersDecycler': 1.0
        })
    )
