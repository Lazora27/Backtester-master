import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
