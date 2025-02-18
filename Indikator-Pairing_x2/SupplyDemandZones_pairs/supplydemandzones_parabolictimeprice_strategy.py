import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
