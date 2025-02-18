import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und WilliamsR
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'WilliamsR': 1.0
        })
    )
