import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
