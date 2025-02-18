import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
