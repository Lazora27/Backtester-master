import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und WilliamsR
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'WilliamsR': 1.0
        })
    )
