import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BarStrength
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BarStrength': 1.0
        })
    )
