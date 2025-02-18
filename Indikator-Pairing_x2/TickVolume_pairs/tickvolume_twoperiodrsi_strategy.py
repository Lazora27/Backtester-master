import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
