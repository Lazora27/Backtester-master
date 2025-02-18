import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
