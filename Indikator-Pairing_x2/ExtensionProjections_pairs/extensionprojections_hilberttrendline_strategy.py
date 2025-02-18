import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HilbertTrendline': 1.0
        })
    )
