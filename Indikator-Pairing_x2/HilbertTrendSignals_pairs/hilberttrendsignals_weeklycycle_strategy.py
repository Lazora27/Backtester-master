import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'WeeklyCycle': 1.0
        })
    )
