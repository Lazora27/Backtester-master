import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
