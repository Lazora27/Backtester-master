import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'EhlersDecycler': 1.0
        })
    )
