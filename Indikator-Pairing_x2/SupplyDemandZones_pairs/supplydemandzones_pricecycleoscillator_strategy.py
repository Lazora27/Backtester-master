import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
