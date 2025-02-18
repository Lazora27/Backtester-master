import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HilbertTrendline': 1.0
        })
    )
