import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DonchianVolatility': 1.0
        })
    )
