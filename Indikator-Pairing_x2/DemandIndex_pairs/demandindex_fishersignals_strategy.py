import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
