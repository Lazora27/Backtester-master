import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CyberCycle': 1.0
        })
    )
