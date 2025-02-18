import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
