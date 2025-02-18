import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
