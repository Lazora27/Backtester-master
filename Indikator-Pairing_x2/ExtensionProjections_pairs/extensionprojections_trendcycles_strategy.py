import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'TrendCycles': 1.0
        })
    )
