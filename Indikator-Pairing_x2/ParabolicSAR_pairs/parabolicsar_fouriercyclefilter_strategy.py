import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
