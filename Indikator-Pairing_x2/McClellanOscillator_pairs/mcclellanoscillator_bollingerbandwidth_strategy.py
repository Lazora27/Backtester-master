import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
