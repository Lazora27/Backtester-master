import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
