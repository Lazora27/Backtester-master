import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ParabolicSAR': 1.0
        })
    )
