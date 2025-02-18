import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'AccelerationBands': 1.0
        })
    )
