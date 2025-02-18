import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
