import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
