import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ProjectionBands': 1.0
        })
    )
