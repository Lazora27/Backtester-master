import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und WilliamsR
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'WilliamsR': 1.0
        })
    )
