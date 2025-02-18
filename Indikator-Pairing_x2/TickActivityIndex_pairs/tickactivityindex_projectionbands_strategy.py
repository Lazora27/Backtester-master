import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
