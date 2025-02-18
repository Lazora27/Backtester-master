import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
