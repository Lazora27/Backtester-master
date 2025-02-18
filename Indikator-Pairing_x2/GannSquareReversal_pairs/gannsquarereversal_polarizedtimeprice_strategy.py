import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
