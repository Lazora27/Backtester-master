import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
