import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BradleySiderograph': 1.0
        })
    )
