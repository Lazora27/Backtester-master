import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
