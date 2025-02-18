import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
