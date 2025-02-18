import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ParabolicSAR': 1.0
        })
    )
