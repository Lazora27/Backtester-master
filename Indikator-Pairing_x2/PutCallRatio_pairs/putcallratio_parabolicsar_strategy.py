import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ParabolicSAR': 1.0
        })
    )
