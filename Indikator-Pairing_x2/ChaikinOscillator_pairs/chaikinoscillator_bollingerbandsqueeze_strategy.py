import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
