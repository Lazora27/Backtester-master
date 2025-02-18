import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
