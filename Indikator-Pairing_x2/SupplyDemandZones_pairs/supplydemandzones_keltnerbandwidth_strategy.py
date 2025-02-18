import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
