import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
