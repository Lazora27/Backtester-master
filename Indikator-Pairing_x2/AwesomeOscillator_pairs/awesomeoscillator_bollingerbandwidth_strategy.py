import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
