import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
