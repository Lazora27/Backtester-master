import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'BollingerPercentB': 1.0
        })
    )
