import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
