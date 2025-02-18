import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AdaptiveATR': 1.0
        })
    )
