import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
