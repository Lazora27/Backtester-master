import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
