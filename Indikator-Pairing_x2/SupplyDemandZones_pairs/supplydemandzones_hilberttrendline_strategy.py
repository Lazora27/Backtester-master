import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HilbertTrendline': 1.0
        })
    )
