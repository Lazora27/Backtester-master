import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TimeCycle
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TimeCycle': 1.0
        })
    )
