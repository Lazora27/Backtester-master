import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
