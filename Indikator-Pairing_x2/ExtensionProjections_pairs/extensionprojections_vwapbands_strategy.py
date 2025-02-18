import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'VWAPBands': 1.0
        })
    )
