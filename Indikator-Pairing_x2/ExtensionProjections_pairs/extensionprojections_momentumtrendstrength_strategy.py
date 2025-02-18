import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
