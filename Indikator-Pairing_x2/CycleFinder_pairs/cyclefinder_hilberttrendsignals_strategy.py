import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
