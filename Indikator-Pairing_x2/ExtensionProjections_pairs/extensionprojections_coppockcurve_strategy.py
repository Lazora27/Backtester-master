import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'CoppockCurve': 1.0
        })
    )
