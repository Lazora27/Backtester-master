import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
