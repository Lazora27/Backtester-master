import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'HilbertTrendline': 1.0
        })
    )
