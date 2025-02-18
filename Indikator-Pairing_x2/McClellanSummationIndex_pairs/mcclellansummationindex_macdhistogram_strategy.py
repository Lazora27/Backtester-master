import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
