import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'GannSquareReversal': 1.0
        })
    )
