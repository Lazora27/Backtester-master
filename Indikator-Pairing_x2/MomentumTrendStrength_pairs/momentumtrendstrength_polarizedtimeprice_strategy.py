import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
