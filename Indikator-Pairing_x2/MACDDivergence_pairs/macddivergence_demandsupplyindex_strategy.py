import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
