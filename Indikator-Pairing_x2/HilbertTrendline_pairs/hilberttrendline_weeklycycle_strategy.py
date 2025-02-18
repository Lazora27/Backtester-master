import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'WeeklyCycle': 1.0
        })
    )
