import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'CycleFinder': 1.0
        })
    )
