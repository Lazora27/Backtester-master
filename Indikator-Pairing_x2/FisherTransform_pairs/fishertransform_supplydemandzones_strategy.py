import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
