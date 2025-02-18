import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'EhlersDecycler': 1.0
        })
    )
