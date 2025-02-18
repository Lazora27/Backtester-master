import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'VolumeOscillator': 1.0
        })
    )
