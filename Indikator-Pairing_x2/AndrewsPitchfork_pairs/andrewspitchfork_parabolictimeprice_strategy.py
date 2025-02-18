import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
