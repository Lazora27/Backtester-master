import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
