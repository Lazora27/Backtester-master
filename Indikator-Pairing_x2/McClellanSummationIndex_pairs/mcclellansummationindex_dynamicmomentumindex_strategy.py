import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
