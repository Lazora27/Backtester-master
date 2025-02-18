import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
