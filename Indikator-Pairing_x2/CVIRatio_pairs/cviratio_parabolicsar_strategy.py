import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ParabolicSAR': 1.0
        })
    )
