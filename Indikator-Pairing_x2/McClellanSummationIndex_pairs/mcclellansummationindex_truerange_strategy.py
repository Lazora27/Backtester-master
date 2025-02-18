import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TrueRange': 1.0
        })
    )
