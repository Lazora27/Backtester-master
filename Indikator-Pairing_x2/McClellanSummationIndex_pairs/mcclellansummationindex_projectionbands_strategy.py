import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
