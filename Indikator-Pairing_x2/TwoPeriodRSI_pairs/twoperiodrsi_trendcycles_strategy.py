import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TrendCycles': 1.0
        })
    )
