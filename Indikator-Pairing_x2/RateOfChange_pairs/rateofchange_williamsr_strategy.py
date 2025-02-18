import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WilliamsR
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WilliamsR': 1.0
        })
    )
