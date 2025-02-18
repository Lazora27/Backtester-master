import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'BollingerBands': 1.0
        })
    )
