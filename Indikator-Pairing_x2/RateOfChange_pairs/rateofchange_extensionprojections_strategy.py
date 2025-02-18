import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ExtensionProjections': 1.0
        })
    )
