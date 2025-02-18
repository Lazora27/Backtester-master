import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AroonIndicator': 1.0
        })
    )
