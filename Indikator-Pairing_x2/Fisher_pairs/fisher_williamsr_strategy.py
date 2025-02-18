import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und WilliamsR
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'WilliamsR': 1.0
        })
    )
