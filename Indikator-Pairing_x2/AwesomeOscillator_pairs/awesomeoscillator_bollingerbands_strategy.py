import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
