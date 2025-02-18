import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
