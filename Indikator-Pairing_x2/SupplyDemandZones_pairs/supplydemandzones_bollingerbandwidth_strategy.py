import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
