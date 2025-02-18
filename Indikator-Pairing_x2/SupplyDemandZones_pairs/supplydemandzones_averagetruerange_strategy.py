import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AverageTrueRange': 1.0
        })
    )
