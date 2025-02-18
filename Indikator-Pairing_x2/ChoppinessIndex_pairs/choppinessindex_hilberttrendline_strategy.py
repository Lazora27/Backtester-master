import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
