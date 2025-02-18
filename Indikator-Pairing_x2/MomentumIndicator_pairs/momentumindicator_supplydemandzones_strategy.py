import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
