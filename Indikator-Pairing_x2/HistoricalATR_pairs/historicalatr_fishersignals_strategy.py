import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'FisherSignals': 1.0
        })
    )
