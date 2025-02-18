import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
