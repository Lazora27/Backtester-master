import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und GannSquares
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'GannSquares': 1.0
        })
    )
