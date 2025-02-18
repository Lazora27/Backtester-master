import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
