import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und WilliamsR
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'WilliamsR': 1.0
        })
    )
