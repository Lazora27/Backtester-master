import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'ProjectionBands': 1.0
        })
    )
