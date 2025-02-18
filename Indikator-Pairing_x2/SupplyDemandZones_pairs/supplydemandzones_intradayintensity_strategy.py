import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'IntradayIntensity': 1.0
        })
    )
