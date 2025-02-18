import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
