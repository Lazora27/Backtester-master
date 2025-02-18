import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MassIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MassIndex': 1.0
        })
    )
