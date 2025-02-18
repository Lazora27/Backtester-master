import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
