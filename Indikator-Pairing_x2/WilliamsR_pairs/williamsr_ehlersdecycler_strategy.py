import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'EhlersDecycler': 1.0
        })
    )
