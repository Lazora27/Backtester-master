import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
