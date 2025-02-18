import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'ExtensionProjections': 1.0
        })
    )
