import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'BollingerBands': 1.0
        })
    )
