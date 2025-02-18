import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'GannSquareReversal': 1.0
        })
    )
