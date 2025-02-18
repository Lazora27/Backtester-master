import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und FisherSignals
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'FisherSignals': 1.0
        })
    )
