import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ProjectionBands': 1.0
        })
    )
