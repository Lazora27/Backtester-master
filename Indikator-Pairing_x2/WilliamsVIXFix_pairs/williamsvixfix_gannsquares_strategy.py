import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und GannSquares
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'GannSquares': 1.0
        })
    )
