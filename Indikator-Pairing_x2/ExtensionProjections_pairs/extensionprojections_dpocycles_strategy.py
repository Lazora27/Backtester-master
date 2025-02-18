import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DPOCycles': 1.0
        })
    )
