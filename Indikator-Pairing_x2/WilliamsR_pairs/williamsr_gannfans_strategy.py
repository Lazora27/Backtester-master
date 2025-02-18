import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und GannFans
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'GannFans': 1.0
        })
    )
