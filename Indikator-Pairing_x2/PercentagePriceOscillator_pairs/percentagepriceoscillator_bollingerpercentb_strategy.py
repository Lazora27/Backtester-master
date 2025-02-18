import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
