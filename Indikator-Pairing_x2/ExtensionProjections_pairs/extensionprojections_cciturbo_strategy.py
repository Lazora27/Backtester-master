import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'CCITurbo': 1.0
        })
    )
