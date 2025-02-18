import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ExtensionProjections': 1.0
        })
    )
