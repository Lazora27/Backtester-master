import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
