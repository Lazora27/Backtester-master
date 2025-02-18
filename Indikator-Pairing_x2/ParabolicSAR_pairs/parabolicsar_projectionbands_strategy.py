import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'ProjectionBands': 1.0
        })
    )
