import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ProjectionBands': 1.0
        })
    )
