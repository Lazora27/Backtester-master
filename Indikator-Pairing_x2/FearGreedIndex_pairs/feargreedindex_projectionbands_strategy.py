import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
