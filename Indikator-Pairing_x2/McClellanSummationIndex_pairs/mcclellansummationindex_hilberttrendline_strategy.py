import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
