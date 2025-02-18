import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
