import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ProjectionBands': 1.0
        })
    )
