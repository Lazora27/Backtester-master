import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und CycleFinder
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'CycleFinder': 1.0
        })
    )
