import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
