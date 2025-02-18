import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
