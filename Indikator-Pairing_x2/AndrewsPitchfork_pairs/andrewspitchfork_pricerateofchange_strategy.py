import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
