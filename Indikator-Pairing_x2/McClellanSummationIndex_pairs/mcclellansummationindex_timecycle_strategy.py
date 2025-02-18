import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
