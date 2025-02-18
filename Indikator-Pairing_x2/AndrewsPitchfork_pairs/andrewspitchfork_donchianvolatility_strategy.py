import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'DonchianVolatility': 1.0
        })
    )
