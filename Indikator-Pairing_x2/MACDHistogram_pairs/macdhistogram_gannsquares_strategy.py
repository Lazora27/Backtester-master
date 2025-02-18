import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und GannSquares
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'GannSquares': 1.0
        })
    )
