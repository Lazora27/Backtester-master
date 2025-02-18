import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
