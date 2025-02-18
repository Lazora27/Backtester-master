import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
