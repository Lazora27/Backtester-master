import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BollingerPercentB': 1.0
        })
    )
