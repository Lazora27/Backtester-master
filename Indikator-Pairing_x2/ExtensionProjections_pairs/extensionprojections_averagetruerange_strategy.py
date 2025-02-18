import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AverageTrueRange': 1.0
        })
    )
