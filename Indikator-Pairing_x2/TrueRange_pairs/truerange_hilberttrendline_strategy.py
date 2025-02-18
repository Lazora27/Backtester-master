import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HilbertTrendline': 1.0
        })
    )
