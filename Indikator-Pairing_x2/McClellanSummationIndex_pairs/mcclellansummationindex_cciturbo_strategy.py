import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
