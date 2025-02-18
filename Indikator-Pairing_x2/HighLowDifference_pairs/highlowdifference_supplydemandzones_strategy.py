import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
