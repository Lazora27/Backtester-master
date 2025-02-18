import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
