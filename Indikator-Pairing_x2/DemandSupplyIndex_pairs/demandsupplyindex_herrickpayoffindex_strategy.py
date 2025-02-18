import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
