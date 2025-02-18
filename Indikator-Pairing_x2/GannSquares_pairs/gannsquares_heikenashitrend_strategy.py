import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
