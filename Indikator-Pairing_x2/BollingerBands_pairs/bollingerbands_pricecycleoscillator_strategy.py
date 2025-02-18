import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
