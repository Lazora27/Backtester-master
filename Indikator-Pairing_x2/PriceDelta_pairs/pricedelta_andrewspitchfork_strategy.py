import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
