import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
