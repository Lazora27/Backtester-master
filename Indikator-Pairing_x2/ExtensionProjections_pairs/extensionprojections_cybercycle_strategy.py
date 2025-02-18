import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'CyberCycle': 1.0
        })
    )
