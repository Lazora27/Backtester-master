import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'DonchianVolatility': 1.0
        })
    )
