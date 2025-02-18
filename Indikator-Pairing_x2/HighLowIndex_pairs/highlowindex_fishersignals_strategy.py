import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
