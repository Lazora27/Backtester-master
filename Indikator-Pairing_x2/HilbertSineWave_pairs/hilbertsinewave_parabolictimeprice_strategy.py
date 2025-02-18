import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
