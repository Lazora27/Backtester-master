import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BollingerBands
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BollingerBands': 1.0
        })
    )
