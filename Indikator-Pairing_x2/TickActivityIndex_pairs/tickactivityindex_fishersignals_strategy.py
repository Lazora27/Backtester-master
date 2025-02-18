import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
