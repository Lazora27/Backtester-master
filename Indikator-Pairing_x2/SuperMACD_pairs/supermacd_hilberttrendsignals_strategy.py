import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
