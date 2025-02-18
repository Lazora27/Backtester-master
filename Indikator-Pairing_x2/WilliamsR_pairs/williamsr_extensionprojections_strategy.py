import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ExtensionProjections': 1.0
        })
    )
