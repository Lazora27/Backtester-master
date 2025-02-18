import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
