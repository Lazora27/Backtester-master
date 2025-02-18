import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'TrendCycles': 1.0
        })
    )
