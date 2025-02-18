import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'AverageLogRange': 1.0
        })
    )
