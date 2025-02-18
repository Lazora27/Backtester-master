import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalAdaptiveCycle_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalAdaptiveCycle und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FractalAdaptiveCycle': {
                'class': FractalAdaptiveCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalAdaptiveCycle'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FractalAdaptiveCycle': 1.0,
            'HilbertTrendline': 1.0
        })
    )
