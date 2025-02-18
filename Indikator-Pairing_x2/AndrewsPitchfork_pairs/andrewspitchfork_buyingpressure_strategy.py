import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'BuyingPressure': 1.0
        })
    )
