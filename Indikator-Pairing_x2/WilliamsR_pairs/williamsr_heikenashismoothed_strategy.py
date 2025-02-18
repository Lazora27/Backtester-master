import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HeikenAshiSmoothed_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HeikenAshiSmoothed
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HeikenAshiSmoothed': 1.0
        })
    )
