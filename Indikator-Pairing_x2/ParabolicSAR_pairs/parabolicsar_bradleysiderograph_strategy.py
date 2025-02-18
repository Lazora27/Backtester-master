import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'BradleySiderograph': 1.0
        })
    )
