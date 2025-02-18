import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'IchimokuCloud': 1.0
        })
    )
