import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'GannSquareReversal': 1.0
        })
    )
