import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
