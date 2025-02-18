import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
