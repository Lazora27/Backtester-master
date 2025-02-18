import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
