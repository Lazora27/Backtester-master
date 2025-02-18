import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und GannSquares
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'GannSquares': 1.0
        })
    )
