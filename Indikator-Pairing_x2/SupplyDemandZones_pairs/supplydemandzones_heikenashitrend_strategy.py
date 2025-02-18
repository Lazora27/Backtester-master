import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
