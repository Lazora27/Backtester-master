import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
