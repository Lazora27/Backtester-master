import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
