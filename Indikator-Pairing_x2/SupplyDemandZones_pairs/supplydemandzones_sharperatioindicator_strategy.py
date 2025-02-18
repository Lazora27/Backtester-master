import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
