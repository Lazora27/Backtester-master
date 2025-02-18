import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
