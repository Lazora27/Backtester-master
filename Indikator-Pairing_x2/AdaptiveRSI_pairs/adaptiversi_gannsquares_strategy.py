import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und GannSquares
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'GannSquares': 1.0
        })
    )
