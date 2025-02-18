import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ParabolicSAR': 1.0
        })
    )
