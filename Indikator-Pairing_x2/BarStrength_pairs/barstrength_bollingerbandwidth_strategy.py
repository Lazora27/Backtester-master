import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
