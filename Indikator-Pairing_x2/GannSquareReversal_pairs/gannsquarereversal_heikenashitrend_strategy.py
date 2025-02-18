import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
