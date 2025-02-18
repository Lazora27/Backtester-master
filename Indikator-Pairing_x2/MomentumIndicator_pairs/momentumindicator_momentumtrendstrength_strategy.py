import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
