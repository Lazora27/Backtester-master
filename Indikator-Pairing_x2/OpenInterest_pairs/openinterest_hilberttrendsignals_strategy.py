import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
