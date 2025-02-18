import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
