import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und GannSquares
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'GannSquares': 1.0
        })
    )
