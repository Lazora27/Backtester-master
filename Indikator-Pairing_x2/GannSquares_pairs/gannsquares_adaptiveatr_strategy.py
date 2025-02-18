import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AdaptiveATR': 1.0
        })
    )
