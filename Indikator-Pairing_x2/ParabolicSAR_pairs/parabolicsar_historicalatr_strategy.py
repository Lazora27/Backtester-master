import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HistoricalATR': 1.0
        })
    )
