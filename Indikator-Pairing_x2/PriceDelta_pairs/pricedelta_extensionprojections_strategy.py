import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ExtensionProjections': 1.0
        })
    )
