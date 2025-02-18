import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'GannSquareReversal': 1.0
        })
    )
