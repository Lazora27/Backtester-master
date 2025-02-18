import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
