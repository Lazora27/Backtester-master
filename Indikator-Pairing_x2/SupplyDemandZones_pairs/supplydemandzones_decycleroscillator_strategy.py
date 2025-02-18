import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
