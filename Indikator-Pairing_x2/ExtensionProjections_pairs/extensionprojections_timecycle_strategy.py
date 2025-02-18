import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'TimeCycle': 1.0
        })
    )
