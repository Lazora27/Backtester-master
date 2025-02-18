import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
