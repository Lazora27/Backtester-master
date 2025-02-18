import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
