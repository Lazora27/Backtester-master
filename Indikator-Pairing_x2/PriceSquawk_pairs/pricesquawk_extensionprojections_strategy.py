import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ExtensionProjections': 1.0
        })
    )
