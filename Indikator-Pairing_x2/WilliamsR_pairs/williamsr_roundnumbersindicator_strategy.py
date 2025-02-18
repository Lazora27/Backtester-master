import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
