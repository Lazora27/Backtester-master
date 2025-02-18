import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
