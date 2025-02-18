import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HilbertSinewave': 1.0
        })
    )
