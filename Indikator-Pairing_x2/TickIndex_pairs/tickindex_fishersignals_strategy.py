import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
