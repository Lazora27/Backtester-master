import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AccelerationBands': 1.0
        })
    )
