import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AAIISentiment': 1.0
        })
    )
