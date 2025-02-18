import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
