import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DemandIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DemandIndex': 1.0
        })
    )
