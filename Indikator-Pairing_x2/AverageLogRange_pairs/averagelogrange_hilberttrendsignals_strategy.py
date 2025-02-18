import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
