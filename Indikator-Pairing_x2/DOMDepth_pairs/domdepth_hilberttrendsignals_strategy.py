import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
