import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'HilbertTrendline': 1.0
        })
    )
