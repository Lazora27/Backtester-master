import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
