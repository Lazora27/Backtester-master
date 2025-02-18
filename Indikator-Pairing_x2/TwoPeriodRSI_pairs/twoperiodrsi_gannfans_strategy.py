import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und GannFans
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'GannFans': 1.0
        })
    )
