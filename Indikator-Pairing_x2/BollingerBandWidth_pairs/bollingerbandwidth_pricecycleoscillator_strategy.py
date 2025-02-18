import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
