import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'GannSquareReversal': 1.0
        })
    )
