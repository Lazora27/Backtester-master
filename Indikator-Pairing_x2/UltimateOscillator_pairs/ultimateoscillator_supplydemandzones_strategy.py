import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
