import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
