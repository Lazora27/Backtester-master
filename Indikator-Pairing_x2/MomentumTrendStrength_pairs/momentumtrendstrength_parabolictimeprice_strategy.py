import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
