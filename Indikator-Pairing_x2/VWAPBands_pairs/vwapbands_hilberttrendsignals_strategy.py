import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
