import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TrendCycles': 1.0
        })
    )
