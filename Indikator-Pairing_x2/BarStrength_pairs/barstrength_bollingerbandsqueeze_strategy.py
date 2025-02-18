import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
